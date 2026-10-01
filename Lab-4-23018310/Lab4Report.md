# COMP 441 Lab 4: Requirements Traceability & Test Management

Requirements source: "Sample Requirements for the Library System" (lecture slide 43, Test Levels, Test Management & Traceability).

## 1. Requirements

| REQ-ID | Area | Requirement | Priority |
|--------|------|-------------|----------|
| REQ-001 | User registration | The system shall allow a new user to register with a unique email address and a password of at least 8 characters | High |
| REQ-002 | User registration | The system shall reject registration when the email address is already in use and display an error message | High |
| REQ-003 | Book search | The system shall allow users to search the catalogue by title, author, or ISBN and return matching results within 2 seconds | High |
| REQ-004 | Book search | The system shall display "No results found" when a search returns no matches | Medium |
| REQ-005 | Book borrowing | A registered user shall be able to borrow up to 3 available books at a time for a 14-day loan period | High |
| REQ-006 | Book borrowing | The system shall prevent borrowing when the user already has 3 books on loan or an overdue item | High |
| REQ-007 | Return processing | The system shall record a return, update book availability, and calculate any overdue fine at P2.00 per day | High |
| REQ-008 | Overdue notifications | The system shall email the user 2 days before the due date and again on each day the book is overdue | Medium |

## 2. Test cases (one positive and one negative per requirement, minimum)

There is no implementation of the Library System, so these are designed cases and have not been executed. Where the requirement text is silent, the expected result is my assumption and is marked (assumption).

| TC ID | REQ | Type | Description / input | Expected result |
|-------|-----|------|---------------------|-----------------|
| TC-001-01 | REQ-001 | Positive | Register with a new email and a 10-character password | Account created |
| TC-001-02 | REQ-001 | Boundary | Register with a new email and exactly 8 characters | Account created |
| TC-001-03 | REQ-001 | Negative | Register with a new email and a 7-character password | Registration rejected |
| TC-002-01 | REQ-002 | Negative | Register with an email that already has an account | Rejected, error message shown |
| TC-002-02 | REQ-002 | Negative | Register with the same email in different letter case | Rejected, error message shown (assumption) |
| TC-002-03 | REQ-002 | Positive | Register with an email not yet in use after a rejected attempt | Account created |
| TC-003-01 | REQ-003 | Positive | Search by an exact title that exists | Matching book returned |
| TC-003-02 | REQ-003 | Positive | Search by an author who has two books in the catalogue | Both books returned |
| TC-003-03 | REQ-003 | Positive | Search by a valid ISBN | Matching book returned |
| TC-003-04 | REQ-003 | Performance | Search a full-size catalogue | Results returned in 2 seconds or less |
| TC-003-05 | REQ-003 | Negative | Search with an empty search term | Not specified, behaviour to be confirmed with the requirement owner |
| TC-004-01 | REQ-004 | Positive | Search for a title that is not in the catalogue | "No results found" displayed |
| TC-004-02 | REQ-004 | Negative | Search for a title that exists | "No results found" is not displayed |
| TC-005-01 | REQ-005 | Positive | User with 0 books borrows an available book | Loan recorded, due date is 14 days from today |
| TC-005-02 | REQ-005 | Boundary | User with 2 books borrows a third available book | Loan recorded |
| TC-005-03 | REQ-005 | Negative | Registered user tries to borrow a book with no copies available | Borrowing refused |
| TC-005-04 | REQ-005 | Negative | A person who is not registered tries to borrow | Borrowing refused |
| TC-006-01 | REQ-006 | Negative | User with 3 books on loan tries to borrow a fourth | Borrowing prevented |
| TC-006-02 | REQ-006 | Negative | User with 1 book on loan and 1 overdue item tries to borrow | Borrowing prevented |
| TC-006-03 | REQ-006 | Positive | User with 2 books on loan, none overdue, tries to borrow | Borrowing allowed |
| TC-007-01 | REQ-007 | Positive | Return a book on the due date | Return recorded, availability increases by 1, fine P0.00 |
| TC-007-02 | REQ-007 | Boundary | Return a book 1 day late | Fine P2.00 |
| TC-007-03 | REQ-007 | Positive | Return a book 3 days late | Fine P6.00 |
| TC-007-04 | REQ-007 | Negative | Return a book that is not on loan | Return rejected, availability unchanged (assumption) |
| TC-008-01 | REQ-008 | Positive | 2 days before the due date | Reminder email sent |
| TC-008-02 | REQ-008 | Positive | 1 day after the due date, then the next day | An email on each day |
| TC-008-03 | REQ-008 | Negative | Book returned before the reminder date | No email sent |
| TC-008-04 | REQ-008 | Negative | 1 day before the due date, when no email is expected | No email sent (assumption: only the 2-days-before reminder) |

## 3. Requirements Traceability Matrix

| Requirement ID | Requirement Description | Test Case ID(s) | Test Level | Status |
|----------------|-------------------------|-----------------|------------|--------|
| REQ-001 | Register with a unique email and a password of 8+ characters | TC-001-01, TC-001-02, TC-001-03 | Unit, System | Designed, not run |
| REQ-002 | Reject duplicate email with an error message | TC-002-01, TC-002-02, TC-002-03 | Integration, System | Designed, not run |
| REQ-003 | Search by title, author or ISBN within 2 seconds | TC-003-01 to TC-003-05 | Integration, System (TC-003-04: performance) | Designed, not run |
| REQ-004 | Show "No results found" for an empty result | TC-004-01, TC-004-02 | System, Acceptance | Designed, not run |
| REQ-005 | Borrow up to 3 available books for 14 days | TC-005-01 to TC-005-04 | Unit, Integration | Designed, not run |
| REQ-006 | Block borrowing at 3 loans or with an overdue item | TC-006-01 to TC-006-03 | Unit, Integration | Designed, not run |
| REQ-007 | Record return, update availability, fine P2.00 per day | TC-007-01 to TC-007-04 | Unit, Integration | Designed, not run |
| REQ-008 | Email 2 days before due and each day overdue | TC-008-01 to TC-008-04 | Integration, System | Designed, not run |

## 4. Mini test plan (REQ-006), IEEE 829 style

- **Test plan identifier:** TP-REQ006-01
- **Item to be tested:** the borrowing rule that prevents a loan when a user has 3 books on loan or an overdue item
- **Features to be tested:** refusal at exactly 3 active loans; refusal when any loan is overdue; borrowing still allowed below 3 loans with nothing overdue
- **Features not tested:** loan period and due date (REQ-005), fine calculation (REQ-007), notifications (REQ-008)
- **Approach:** integration-level tests against the loan service with prepared user and loan data (TC-006-01 to TC-006-03)
- **Scope:** the loan eligibility check and the message returned to the user
- **Entry criteria:** borrowing (REQ-005) is implemented; test users with 2 and 3 loans and one overdue loan can be set up; test environment is available
- **Exit criteria:** all three test cases pass; no open defect of High severity or above on REQ-006
- **Suspension criteria:** testing stops if loans cannot be created or the loan service is unavailable
- **Deliverables:** test results, defect log, updated RTM status

## 5. Defect log (two sample defects, full lifecycle)

The Library System has no implementation, so these two sample defects are real defects from the Task Manager sample repo (Lab 1 D04 and D05). Do the lifecycle in GitHub Issues (or a spreadsheet) and replace each `<date>` with the date you actually performed the stage.

### Defect 1: pending list skips the first task (Lab 1 D04)

| Stage | Date | Notes |
|-------|------|-------|
| New | `<date>` | `get_pending_tasks` skips index 0 because the loop starts at `range(1, ...)`. `test_get_pending_tasks_includes_first_task` fails |
| Triaged | `<date>` | **Severity: High** (wrong results for every user). **Priority: High** (core feature) |
| Assigned | `<date>` | Assigned to Miguel |
| Fixed | `<date>` | Loop replaced with `[task for task in tasks if not task["done"]]` |
| Verified | `<date>` | The test now passes |
| Closed | `<date>` | Fix committed and pushed; issue closed |

### Defect 2: average priority crashes on an empty list (Lab 1 D05)

| Stage | Date | Notes |
|-------|------|-------|
| New | `<date>` | `average_priority([])` raises `ZeroDivisionError`. `test_average_priority_of_empty_list` fails |
| Triaged | `<date>` | **Severity: High** (crash). **Priority: Medium** (only with an empty list) |
| Assigned | `<date>` | Assigned to Miguel |
| Fixed | `<date>` | Added `if not tasks: return 0` |
| Verified | `<date>` | The test now passes |
| Closed | `<date>` | Fix committed and pushed; issue closed |

Evidence: before the fixes `tests/test_tasks.py` shows 4 passed, 2 failed; after them it shows 6 passed (`Lab4Fixes.patch`). Your Lab 3 file `test_discount.py` still shows its 7 intentional failures.

## 6. AI-generated RTM vs. mine

**Do this step in your own assistant**, then fill in the table from what it actually returned.

Prompt: *"Here are the requirements for a library system: [paste the table from section 1]. Produce a requirements traceability matrix with columns Requirement ID, Requirement Description, Test Case ID(s), Test Level, Status."*

Things to check:
- Does it cover all 8 requirements?
- Does it have at least two test cases per requirement, one positive and one negative?
- Do the test levels make sense (for example, performance for the 2-second search)?
- Does it mark a status as Pass or Done for tests that were never run?
- Does it catch the gaps in the requirements, such as an empty search term or the due date itself for notifications?

| Aspect | AI matrix | My matrix |
|--------|-----------|-----------|
| Completeness | | |
| Positive and negative cases | | |
| Test levels | | |
| Statuses | | |
| Requirement gaps noticed | | |

## 7. Reflection (write this yourself)

Question: *Where did the AI-generated traceability matrix diverge from yours, and which version would you trust for an audit?*

Base your answer on the table in section 6.