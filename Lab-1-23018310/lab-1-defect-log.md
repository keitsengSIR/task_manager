# COMP 441 — Lab 1: Manual Defect Log

Repository: task-manager (Python). 
Files reviewed: `app/tasks.py`, `app/storage.py`, `app/cli.py`, `tests/test_tasks.py`.

## 1. Defect Log

"Verified" = I ran the code and reproduced it. "Read" = found by reading only.

ID:D01	File:app/storage.py	Line:4	Description: Hard-coded API key committed in source Credential leak.	Sev:Critical	How found:Read
ID:D02	File:app/storage.py	Line:26	Description: SQL built by string concatenation with title_filter, so it is open to SQL injection Needs parameterised queries.	Sev:Critical	How found:Read
ID:D03	File:app/storage.py	Line:11	Description: "Task #" + task["id"] concatenates str + int, raising TypeError. The CLI crashes as soon as one task exists.	Sev:High	How found:Verified
ID:D04	File:app/tasks.py	Line:48	Description: range(1, len(tasks)) starts at 1, so the first task is never returned by get_pending_tasks.	Sev:High	How found:Verified (test fails: 1 != 2)
ID:D05	File:app/tasks.py	Line:59	Description: average_priority([]) divides by zero (ZeroDivisionError). No empty-list guard.	Sev:High	How found:Verified (test fails)
ID:D06	File:app/tasks.py	Line:26	Description: id = len(tasks) + 1 produces duplicate IDs after a removal (tasks 1,2 -> remove 1 -> new task also gets id 2). complete_task and remove_task then hit the wrong task.	Sev:High	How found:Verified (ids: [2, 2])
ID:D07	File:app/tasks.py	Line:23	Description: Mutable default argument tags=[] is shared across calls, so tags added to one task appear on all others.	Sev:High	How found:Verified
ID:D08	File:app/tasks.py	Line:11-13	Description: File opened without 'with' and never closed (resource leak).	Sev:Medium	How found:Read
ID:D09	File:app/tasks.py	Line:12	Description: json.load has no error handling. A corrupt or empty tasks.json crashes the app on startup.	Sev:Medium	How found:Read
ID:D10	File:app/tasks.py	Line:5	Description: TASKS_FILE is a relative path, so data is loaded from or saved to whichever directory the app is run in.	Sev:Medium	How found:Read
ID:D11	File:app/storage.py	Line:18-21	Description: days_until_due subtracts now() (with time of day) from midnight, so a task due today returns -1 (off by one).	Sev:Medium	How found:Verified (-1)
ID:D12	File:app/cli.py	Line:2, 6-11	Description: CLI only loads and prints. save_tasks and add_task are imported but unused and there is no way to add or complete tasks, so the main features can't be exercised.	Sev:Medium	How found:Read
ID:D13	File:app/tasks.py	Line:77-82	Description: calculate_discount has no validation (negative price, non-bool is_premium), a magic number (0.8), and float rounding. '== True' is non-idiomatic.	Sev:Low	How found:Read
ID:D14	File:app/tasks.py	Line:62-66	Description: find_task_by_title implicitly returns None, is case-sensitive, and callers aren't warned.	Sev:Low	How found:Read
ID:D15	File:app/tasks.py	Line:69-74	Description: remove_task silently does nothing when the id doesn't exist and gives no success/failure result (unlike complete_task).	Sev:Low	How found:Read
ID:D16	File:tests/test_tasks.py	Line:N/A	Description: No tests for remove_task, find_task_by_title, load/save_tasks, days_until_due, format_task_report or build_query. This is why D03, D06 and D11 go unnoticed.	Sev:Low	How found:Read

## 2. Existing test suite results

Command: `pytest`

- Total tests: **6**
- Passed: **4**
- Failed: **2**
  - `test_get_pending_tasks_includes_first_task` (D04, off-by-one)
  - `test_average_priority_of_empty_list` (D05, ZeroDivisionError)

## 3. Tool versions

Captured on my machine (screenshot attached in submission folder as `tool-versions.png`):

![alt text](image.png)

- Git: 2.55.0.windows.5
- Python: 3.14.3
- pip: 25.3

![alt text](image-1.png)
![alt text](image-2.png)

AI assistant confirmation: 
## 4. Reflection 

Reflection

Several of the defects I logged would be caught quickly by a linter or an automated test. D04 (the off-by-one in get_pending_tasks) and D05 (division by zero in average_priority) are already caught by the existing test suite, which fails on both. A linter such as pylint would flag D07 (mutable default argument tags=[]) as a dangerous default value, D08 (file opened without "with") as a resource-handling issue, and D13 (comparison "== True") as a style issue. The hard-coded API key (D01) and the SQL injection (D02) would be caught by a secret scanner or a security tool such as Semgrep or Bandit, although a basic linter would miss them. D03 (concatenating a string with an integer) would crash as soon as any test or run reached format_task_report with data, but no such test exists, so it currently goes unnoticed.


