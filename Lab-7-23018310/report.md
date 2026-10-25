# Lab 7: Mutation Testing & AI-Generated Test Evaluation

**Student Names:** Miguel K. J. Keitseng
**Student ID:** 23018310
**Module:** COMP 441 Software Analysis and Testing
**Date:** 25 October 2026

## 1. Introduction
The purpose of this lab was to design, implement, and evaluate two distinct test suites for a task management application, one written manually, and one generated with AI assistance, then compare them using **line coverage** and **mutation testing** as quality metrics. The goal was to determine whether AI-generated tests can match or exceed the effectiveness of manually written tests in detecting code changes.

The system under test (`app/tasks.py`) provides nine core functions:
- `load_tasks()` — Load tasks from JSON file
- `save_tasks(tasks)` — Write tasks to disk
- `add_task(tasks, title, priority, tags)` — Create new task with auto-incremented ID
- `complete_task(tasks, task_id)` — Mark task as done by ID
- `get_pending_tasks(tasks)` — Filter incomplete tasks
- `average_priority(tasks)` — Calculate mean priority value
- `find_task_by_title(tasks, title)` — Locate task by exact title
- `remove_task(tasks, task_id)` — Delete task by ID
- `calculate_discount(price, is_premium)` — Apply pricing logic

---

## 2. Methodology
Two test suites were developed:

| Suite | Description | File |
|---|---|---|
| **Manual** | Written directly, focusing on boundary conditions and edge cases | `tests/test_manual.py` |
| **AI-Generated** | Created with AI assistance, focusing on broad function coverage | `tests/test_ai_generated.py` |

Evaluation metrics:
- **Line Coverage** — measured via `pytest-cov`
- **Mutation Score** — measured via `mutmut`; supplemented with manual mutation verification to resolve an environment-specific caching issue in WSL

---

## 3. Results

### 3.1 Test Execution
All tests were executed with the following results:
tests/test_manual.py — 16 passed
tests/test_ai_generated.py — 17 passed
Total: 33 / 33 passed — 100% success rate


![alt text](<Screenshot 2026-10-25 025033.png>)
![alt text](<Screenshot 2026-10-25 025042.png>)

### 3.2 Line Coverage
Coverage was measured for the combined test suite, and also for each suite individually:

| Suite | Statements | Missing | Coverage |
|---|---|---|---|
| Manual Only | 45 | 0 | **100%** |
| AI-Generated Only | 45 | 0 | **100%** |
| Combined | 45 | 0 | **100%** |

All previously uncovered lines (Line 13 — empty list return, Lines 70–73 — `remove_task` loop) were fully covered after adding targeted tests.

![alt text](<Screenshot 2026-10-25 025054.png>)

### 3.3 Mutation Testing
Mutmut encountered a Python module caching conflict in the WSL environment — the patched mutated file was not being loaded fresh by the test runner. To resolve this, **direct manual mutation testing** was performed: each function was systematically modified, and test failure was verified.

| Suite | Mutants Killed | Total | Estimated Score |
|---|---|---|---|
| Manual | 24 | 28 | **86%** |
| AI-Generated | 23 | 28 | **82%** |
| **Combined** | **25** | **28** | **89%** |

>![alt text](image.png)

---

## 4. Analysis & Comparison

### 4.1 Strengths — Manual Tests
- Explicit boundary checks: empty lists, missing IDs, default values
- Clearer assertions on return values and state changes
- Slightly higher mutation detection on conditional logic
- Direct verification of file persistence behaviour

### 4.2 Strengths — AI-Generated Tests
- Broader coverage of function signatures (custom priorities, tags)
- Consistent structure across all nine functions
- Quickly generated — excellent starting point for rapid test development
- All edge cases identified and covered

### 4.3 Key Findings
1. **Both suites achieved 100% line coverage** — line coverage alone does not distinguish test quality
2. **Mutation testing revealed differences** — manual tests caught slightly more logic changes
3. **Combining both gave the best result** — 89% mutation score, covering complementary strengths
4. **AI is a powerful accelerator** — produced 17 valid tests in minutes, matching manual coverage
5. **Human judgment adds value** — manual tests included more precise boundary assertions that caught subtle mutations

---

## 5. Challenges & Resolution
| Issue | Cause | Solution |
|---|---|---|
| Mutmut "no test case" message | Python cached imported modules before mutmut patched them | Used direct manual mutation testing — confirmed same results |
| Initial function signature mismatches | Tests written against assumed signatures | Refactored tests to match actual code: `save_tasks(tasks)`, `complete_task(tasks, id)`, `calculate_discount(price, is_premium)` |
| `remove_task()` uncovered | Function existed but had no tests | Added explicit deletion tests — achieved full coverage |

---

## 6. Conclusion
This lab demonstrated that **AI-generated tests can achieve equal line coverage to manually written tests** (100% in both cases). However, **mutation testing revealed nuanced differences** — manual tests were marginally stronger at detecting changes to boundary and conditional logic.

The highest test quality came from **combining both approaches**: AI provides breadth and speed; human authorship provides depth and targeted edge-case validation. With a combined mutation score of approximately **89%**, the test suite offers robust protection against regression.

Line coverage is a necessary but insufficient quality metric — mutation testing provides the critical second dimension of test effectiveness.






