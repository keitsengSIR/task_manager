# COMP 441 Lab 3: Dynamic Analysis & Test Design Techniques

Target function: `calculate_discount(price, is_premium)` in `app/tasks.py`. Tests: `test_discount.py` (pytest). Results: `test_results.txt`.

## 1. Specification used

No separate specification was supplied, so this one is derived from the function's docstring ("Apply a loyalty discount for premium users"). **If your lecturer gave a different spec, replace this section and adjust the tables.**

- `price`: int or float, valid domain `price >= 0`
- `is_premium`: `bool`
- Premium users pay 80% of the price (a 20% discount); other users pay the full price
- Invalid input must raise `ValueError` (bad value) or `TypeError` (bad type) instead of returning a result

The first three points come from the code and docstring. The last point (reject invalid input) is my assumption, because the docstring is silent on it.

## 2. Equivalence-partition table

| Input | Class | Type | Representative value |
|-------|-------|------|----------------------|
| price | P1: number >= 0 | Valid | 100, 19.99 |
| price | P2: number < 0 | Invalid | -100 |
| price | P3: non-numeric string | Invalid | "100" |
| price | P4: None | Invalid | None |
| is_premium | S1: True | Valid | True |
| is_premium | S2: False | Valid | False |
| is_premium | S3: None | Invalid | None |
| is_premium | S4: non-bool string | Invalid | "yes" |
| is_premium | S5: non-bool int | Invalid | 1 |

## 3. Boundary-value table

| Input | Boundary | Just outside | On boundary | Just inside |
|-------|----------|--------------|-------------|-------------|
| price | lower, 0 | -0.01 | 0 | 0.01 |
| price | upper | no upper limit in spec; a very large value (1,000,000,000) is used as an extreme | n/a | 1,000,000,000 |

## 4. Test design (15 cases)

| TC | price | is_premium | Partition / boundary | Expected | Actual | Result |
|----|-------|------------|----------------------|----------|--------|--------|
| TC01 | 100 | True | P1, S1 | 80 | 80 | Pass |
| TC02 | 100 | False | P1, S2 | 100 | 100 | Pass |
| TC03 | 0 | True | price lower boundary | 0 | 0 | Pass |
| TC04 | 0 | False | price lower boundary | 0 | 0 | Pass |
| TC05 | 0.01 | True | just inside boundary | 0.008 | 0.008 | Pass |
| TC06 | 19.99 | True | P1, decimal | 15.992 | 15.992 | Pass |
| TC07 | 1,000,000,000 | True | extreme large value | 800,000,000 | 800,000,000 | Pass |
| TC08 | -0.01 | True | just outside boundary, P2 | ValueError | returned -0.008 | **Fail** |
| TC09 | -100 | False | P2 | ValueError | returned -100 | **Fail** |
| TC10 | "100" | True | P3 | TypeError | TypeError (raised by accident, by `str * float`) | Pass |
| TC11 | "100" | False | P3 | TypeError | returned "100" | **Fail** |
| TC12 | None | False | P4 | TypeError | returned None | **Fail** |
| TC13 | 100 | None | S3 | TypeError | returned 100 | **Fail** |
| TC14 | 100 | "yes" | S4 | TypeError | returned 100 | **Fail** |
| TC15 | 100 | 1 | S5 | TypeError | returned 80.0 | **Fail** |

## 5. Results

Run with `pytest tests/test_discount.py -v` against the original `calculate_discount`: **15 tests, 8 passed, 7 failed.**

Defects revealed:

- **D-A (TC08, TC09):** negative prices are accepted and produce negative results. No validation.
- **D-B (TC11, TC12):** non-numeric prices are silently returned for regular users. The same bad input raises `TypeError` for premium users (TC10) only as a side effect of the multiplication, so behaviour is inconsistent.
- **D-C (TC13, TC14):** a missing or wrong-typed `is_premium` (None, "yes") is treated as "not premium" with no error.
- **D-D (TC15):** the integer 1 is treated as premium, because `1 == True` in Python.

All of these stem from the missing input validation noted as D13 in Lab 1. The pass/fail split depends on my assumed spec: if the intended behaviour is not to validate input, TC08 to TC15 would not be defects.

## 6. AI-generated equivalence classes and boundaries

Prompt given to the assistant (use this in your own assistant for this step):

> Here is a function specification: `calculate_discount(price, is_premium)` gives premium users (bool True) 20% off a non-negative numeric price and leaves other users' prices unchanged. Generate equivalence classes and boundary/edge-case test data for both inputs.

**Fill this section from your own assistant session.** Below is a response generated in this chat from the same prompt, which you can use as a starting point if you verify it yourself.

AI equivalence classes: price valid (>= 0), price negative, price non-numeric, price None, price NaN/infinity, price bool; is_premium True, False, truthy non-bool (1, "yes"), falsy non-bool (0, None, "").
AI boundary values: -0.01, 0, 0.01, very large float (1e308).

### Comparison with my manual set

| Aspect | Result |
|--------|--------|
| Overlap | Valid and negative price classes, True/False, and the -0.01 / 0 / 0.01 boundaries were produced by both |
| Gaps in my set found by the AI | NaN and infinity; bool as a price; falsy non-bool values for `is_premium` (0, "") |
| Gaps in the AI set | No explicit decimal/rounding case like 19.99; non-numeric price listed as one class, which hides that premium and regular users behave differently (TC10 vs TC11) |
| Unsupported by the spec | The AI's expected results for NaN, infinity and the 1e308 boundary are not defined by the specification, so they are assumptions, not correct answers |

## 7. Reflection

Question: What proportion of your manually designed boundary cases did the AI assistant reproduce, and what did it miss or get wrong?

The AI reproduced the three price boundary values around zero (-0.01, 0, 0.01), which is 3 of my 4 boundary-type cases. It missed my extreme large price case and the decimal 19.99 case. It also added edge cases I had not considered (NaN, infinity, bool and falsy values) but assigned them expected outputs the specification never defined. It also grouped all non-numeric prices into one class, which hid the inconsistency between premium and regular users that my separate test cases exposed. So the AI is useful for widening coverage, but I still had to check its expected values against the specification.