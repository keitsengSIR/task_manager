# Lab 6: AI-Generated Test Cases & Coverage Delta
**Student ID:** 23018310
**Module:** COMP 441 Software Analysis and Testing
**Date:** 2 October 2026

---

## 1. Lab Overview & Objectives
The purpose of this lab was to:
- Select three functions from the codebase that had no existing tests
- Generate unit tests for them using an AI assistant
- Write equivalent tests manually without AI assistance
- Measure and compare coverage percentage, assertion count, and assertion strength
- Evaluate the trade-offs between AI-generated and human-written test suites

Functions under test:
| Function | Purpose |
|---|---|
| `load_tasks()` | Reads saved tasks from disk; returns empty list if no file exists |
| `save_tasks()` | Writes the current task list to a JSON file |
| `find_task_by_title()` | Returns the first task matching the given title, or `None` if not found |

---

## 2. AI Assistant Configuration
- **Tool Used:** Claude (free-tier web interface)
- **Date:** 2 October 2026
- **Prompt Text:**
> Here are three functions from app/tasks.py:
> 
> def load_tasks():
>     """Load tasks from disk, returning an empty list if no file exists."""
>     if os.path.exists(TASKS_FILE):
>         with open(TASKS_FILE, "r", encoding="utf-8") as f:
>             return json.load(f)
>     return []
> 
> def save_tasks(tasks):
>     """Persist tasks to disk."""
>     with open(TASKS_FILE, "w") as f:
>         json.dump(tasks, f)
> 
> def find_task_by_title(tasks, title):
>     """Return the first task matching the given title."""
>     for task in tasks:
>         if task["title"] == title:
>             return task
> 
> Write pytest unit tests for these three functions. Use temporary files so tests don't affect real data. Include tests for:
> - load_tasks returns empty list when file doesn't exist
> - load_tasks correctly reads saved data
> - save_tasks writes data that can be read back
> - find_task_by_title finds an existing task
> - find_task_by_title returns None when not found

![alt text](<Screenshot 2026-10-02 232946.png>)
![alt text](<Screenshot 2026-10-02 232951.png>)

## 3. Test Implementation

### 3.1 AI-Generated Test Suite
**File:** `tests/test_ai_generated.py`
- 5 test functions
- Uses `monkeypatch` to redirect `TASKS_FILE` to a temporary test file
- Cleans up after each run
- Focuses on basic return values and equality matching

### 3.2 Manually Written Test Suite
**File:** `tests/test_manual.py`
- 7 test functions
- Same fixture pattern for isolation and cleanup
- Includes additional scenarios:
  - Verifying all individual fields survive a save/load round-trip
  - Case sensitivity of title matching
  - Behaviour with empty task lists
  - Explicit file creation confirmation


## 4. Coverage Results

### 4.1 AI-Only Coverage

- **Total Project Coverage:** 29%
- **app/tasks.py Coverage:** 47%
- **Tests Passed:** 5 / 5
- **Assertions:** ~10

![alt text](<Screenshot 2026-10-02 233619.png>)

### 4.2 Manual-Only Coverage2
- **Total Project Coverage:** 29%
- **app/tasks.py Coverage:** 47%
- **Tests Passed:** 7 / 7
- **Assertions:** ~17

![alt text](<Screenshot 2026-10-02 233619.png>)

### 4.3 Combined Suite Coverage
- **Total Project Coverage:** 29%
- **app/tasks.py Coverage:** 47%
- **Tests Passed:** 7 / 7
- **Assertions:** ~17


### 4.3 Combined Suite Coverage
- **Total Project Coverage:** 29%
- **app/tasks.py Coverage:** 47%
- **Tests Passed:** 12 / 12
- **Assertions:** 27 total

![alt text](<Screenshot 2026-10-02 233619.png>)

## 5. Comparison Table

| Metric | AI-Generated | Manual | Combined |
|---|---|---|---|
| **Project Coverage %** | 29% | 29% | 29% |
| **tasks.py Coverage %** | 47% | 47% | 47% |
| **Tests Executed** | 5 | 7 | 12 |
| **Number of Assertions** | ~10 | ~17 | 27 |
| **Assertion Strength** | Weak — checks return value equality; does not validate individual fields or edge cases | Strong — validates every field, data integrity, edge cases, and behaviour under different conditions | — |
| **Key Strengths** | Fast generation; clean, readable structure; minimal setup | Thorough scenario coverage; deeper validation; considers what could go wrong | Complementary coverage |
| **Key Gaps** | Misses edge cases; treats returned object as a "black box" without inspecting internals | Takes longer to design and implement | — |

## 6. Analysis & Reflection

### 6.1 Coverage Interpretation
Both test suites achieved identical coverage percentages — **47%** on `app/tasks.py` and **29%** across the whole project. This was expected: both suites targeted exactly the same three previously-untested functions. The remaining 53% of `tasks.py` consists of functions covered in earlier labs (`add_task`, `complete_task`, etc.) and was outside the scope of this lab. Files such as `cli.py` and `storage.py` remain uncovered because they were not part of the assigned functions.

### 6.2 Assertion Quality
The meaningful difference was not in coverage lines but in **assertion depth**. The AI-generated tests were sufficient to "light up" coverage — they confirmed that functions returned something that matched expectations at a surface level. However, they did not verify that *all* data was preserved correctly. For example, after saving and reloading a task, the AI test only checked that the list matched — it did not confirm that fields like `priority`, `tags`, or `done` status survived the round-trip.

My manual tests were designed to answer a different question: not just "does it return without crashing?" but "is the result *correct in every detail*?" I added tests for case sensitivity, empty lists, and field-by-field integrity checks — scenarios the AI did not mention.

### 6.3 Reflection Question
> Did the AI-generated tests achieve high coverage with weak assertions? Give a concrete example.

**Yes.** The AI suite achieved the same coverage percentage as the manual suite but with significantly weaker assertions. A concrete example is `test_load_tasks_reads_saved_data` in the AI-generated file: it creates a task list, saves it, loads it back, and asserts `assert result == data`. This passes if the returned structure matches — but it does not verify that individual attributes like `priority` or `tags` are correctly preserved. If a bug caused those fields to be dropped or corrupted during save/load, this test would still pass as long as the outer list structure remained the same.

This demonstrates an important distinction: **coverage measures whether code is executed, not whether it is correct.** AI tools can produce tests that execute code quickly, but they do not yet reliably understand what full correctness looks like. Human-written tests, while slower to create, reflect genuine insight into the system's behaviour and edge cases. The strongest approach is to combine both: use AI to generate initial coverage quickly, then review and strengthen those tests with human judgment.

