# Lab 9 — Timestamped Session Log

**Start Time:**  14:30
**End Time:**    15:15
**Duration:**    45 minutes

---

## AI-Suggested Exploratory Testing Ideas

### 1. Data — Boundary & Edge Values
**Focus:** What happens when task data is unusual or extreme?
- Add a task with empty/blank title → check if it saves and displays
- Add a task with very long title (50+ characters) → check display breaks or truncates
- Add tasks with special characters (`<script>`, `$SHELL`, emojis) → check storage and output
- Set priority to 0, negative number, or very large value → check validation/calculation
- Add 100+ tasks → check listing performance and pagination

### 2. Function — State Transitions
**Focus:** How does task status change behave?
- Complete the same task twice → check for error or silent duplicate
- Complete a non-existent task ID → check error handling vs crash
- Mark task as complete, then add another → verify pending count updates correctly
- Complete all tasks → verify pending list is truly empty
- Add → complete → add again → check IDs don't conflict or reset

### 3. Operations — Sequences & Interruptions
**Focus:** How does the app behave through realistic usage patterns?
- Add task → exit without saving → run app again → task should NOT persist
- Add task → save → delete file externally → run app → should handle missing file gracefully
- Rapid-fire: add → add → complete → list → save → list → check no race conditions
- Run multiple app instances simultaneously → check file locking/corruption
- Save → modify JSON file manually → load → check malformed data is handled

### 4. Time — Persistence & Consistency
**Focus:** Does data survive across sessions and changes?
- Add tasks → note counts → reopen app → verify counts match exactly
- Add tasks → change system date/time → reopen → check timestamps or behaviour unaffected
- Leave app running for a few minutes → check no memory leaks or slowdown
- Save → reopen → complete → save → reopen → confirm state persists step-by-step
- Test with empty storage → normal usage → many tasks → verify all states work

### 5. Structure & Platform — Interface & Environment
**Focus:** CLI behaviour and system interactions
- Run app from different directories → confirm storage path still works
- Check output formatting with 0 tasks, 1 task, many tasks → no misalignment
- Check no sensitive data (passwords, paths) exposed in error messages
- Test copy-paste input → extra spaces, leading/trailing whitespace → trimming behaviour
- Verify exit codes → 0 on success, non-zero on errors

---

## Session Log

| Time   | Area                          | Observation                                                                 | Source | Severity |
|--------|-------------------------------|-----------------------------------------------------------------------------|--------|----------|
| 14:32  | Data — Empty State            | Clear message: "Loaded 0 tasks" + "No tasks currently stored" displayed     | AI     | —        |
| 14:33  | Time — Persistence            | Output identical on repeated runs — consistent across sessions            | AI     | —        |
| 14:33  | Data — File Check             | No `tasks.json` found — app shows 0 tasks without crashing                 | AI     | —        |
| 14:34  | Ops — Missing File            | Graceful handling — no crash, no error message displayed                   | AI     | —        |
| 14:35  | Structure — Import Interface  | `save_tasks` not in `app.storage` — location differs from expected         | AI     | —        |
| 14:36  | Structure — Storage Module   | `storage.py` has NO save/load functions — only helpers exist               | AI     | High     |
| 14:36  | Function — Data Persistence   | No save/load via expected module path — data cannot be persisted           | AI     | High     |
| 14:37  | Security — SQL Injection      | `build_query()` uses string concatenation — vulnerability if connected    | Self   | High     |
| 14:37  | Structure — Module Layout     | Persistence lives in `app.tasks`, not `app.storage`                        | AI     | —        |
| 14:39  | Structure — Type Mismatch     | `format_task_report()` crashes — `task["id"]` is int, code expects str     | AI     | High     |
| 14:41  | Data — ID Generation          | IDs assigned correctly: `[1, 2]` — sequential, no duplicates              | AI     | —        |
| 14:43  | Function — Complete Task      | Works: returns True, pending count dropped 2 → 1                           | AI     | —        |
| 14:44  | Function — Double Complete    | Re-completing completed task returns True — should be False                | AI     | Medium   |
| 14:45  | Function — Invalid ID         | Complete task 999 returns False — handled gracefully                       | AI     | —        |
| 14:47  | Data — Blank Title            | Empty title `''` saves successfully — no input validation                 | Self   | Medium   |
| 14:48  | Function — Find by Title      | Works perfectly — returns full matching task object                        | Self   | —        |
| 14:49  | Function — Average Priority   | Calculates correctly: `1.0`                                                | Self   | —        |
| 14:51  | Function — Remove Task        | Returns `None`, task not removed — function non-functional                | Self   | High     |
| 14:53  | Function — Remove Invalid ID  | Removing 999 also returns `None` — no feedback, no removal                 | Self   | High     |

---

## Bug Summary

| ID   | Description                                          | Severity | Source |
|------|------------------------------------------------------|----------|--------|
| B-01 | `format_task_report()` crashes — int/str type error  | High     | AI     |
| B-02 | Double-complete returns True — logic flaw            | Medium   | AI     |
| B-03 | Empty title saves — no input validation              | Medium   | Self   |
| B-04 | `remove_task()` returns `None` — does nothing        | High     | Self   |

---

## Source Breakdown

| Source                  | Bugs Found | Percentage |
|-------------------------|------------|------------|
| AI-suggested avenues    | 2          | 50%        |
| Self-found / unprompted | 2          | 50%        |
| **Total**               | **4**      | **100%**   |