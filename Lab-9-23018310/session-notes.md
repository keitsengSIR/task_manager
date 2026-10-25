 ## AI-Suggested Exploratory Testing Ideas

## 1. Data — Boundary & Edge Values
Focus: What happens when task data is unusual or extreme?
Add a task with empty/blank title → check if it saves and displays
Add a task with very long title (50+ characters) → check display breaks or truncates
Add tasks with special characters (<script>, $SHELL, emojis) → check storage and output
Set priority to 0, negative number, or very large value → check validation/calculation
Add 100+ tasks → check listing performance and pagination

## 2. Function — State Transitions
Focus: How does task status change behave?
Complete the same task twice → check for error or silent duplicate
Complete a non-existent task ID → check error handling vs crash
Mark task as complete, then add another → verify pending count updates correctly
Complete all tasks → verify pending list is truly empty
Add → complete → add again → check IDs don't conflict or reset

## 3. Operations — Sequences & Interruptions
Focus: How does the app behave through realistic usage patterns?
Add task → exit without saving → run app again → task should NOT persist
Add task → save → delete file externally → run app → should handle missing file gracefully
Rapid-fire: add → add → complete → list → save → list → check no race conditions
Run multiple app instances simultaneously → check file locking/corruption
Save → modify JSON file manually → load → check malformed data is handled

## 4. Time — Persistence & Consistency
Focus: Does data survive across sessions and changes?
Add tasks → note counts → reopen app → verify counts match exactly
Add tasks → change system date/time → reopen → check timestamps or behaviour unaffected
Leave app running for a few minutes → check no memory leaks or slowdown
Save → reopen → complete → save → reopen → confirm state persists step-by-step
Test with empty storage → normal usage → many tasks → verify all states work

## 5. Structure & Platform — Interface & Environment
Focus: CLI behaviour and system interactions
Run app from different directories → confirm storage path still works
Check output formatting with 0 tasks, 1 task, many tasks → no misalignment
Check no sensitive data (passwords, paths) exposed in error messages
Test copy-paste input → extra spaces, leading/trailing whitespace → trimming behaviour
Verify exit codes → 0 on success, non-zero on errors

## Timer:

Start Time:  14:30
End Time:    15:15

# LOG

Time	Area	Observation	Source
14:32	Data — Empty state	Clear message: "Loaded 0 tasks" + "No tasks currently stored" displayed	AI
14:33	Time — Persistence	Output identical on both runs: "Loaded 0 tasks" / "Pending tasks: 0" — consistent	AI
14:33	Data — File check	No tasks.json found — only package.json and package-lock.json exist. App still shows 0 tasks without crashing	AI
14:34	Ops — Missing file	Graceful handling: No tasks.json exists, app loads cleanly and shows 0 tasks — no crash, no error	AI
14:35	Structure — Import interface	BUG: Cannot import save_tasks from app.storage — function name may differ or be missing	AI
14:36	Structure — Storage module	BUG: storage.py has NO save/load functions! Contains only formatting, date calculation, and query building — cannot persist tasks at all	AI
14:36	Function — Data persistence	BUG: No way to save tasks to disk — app will always show 0 tasks, changes are lost on exit	AI
14:37	Security — SQL injection risk	OBS: build_query() concatenates strings directly — SQL injection vulnerability if used with real DB	Self-found
14:37	Structure — Module layout	OBS: save_tasks and load_tasks are in app.tasks, NOT in app.storage — different location than expected	AI
14:37	Structure — storage.py role	OBS: storage.py only has helpers (formatting, dates, queries) — actual persistence lives in tasks.py	AI
14:39	Structure — Type mismatch	BUG: format_task_report() crashes — task["id"] is an integer but code treats it as string. Error: can only concatenate str (not "int") to str	AI	High
14:41	Data — ID generation	IDs assigned correctly: [1, 2] — sequential integers, no duplicates	AI	—
14:41	Structure — Root cause confirmed	BUG confirmed: task["id"] is int, but format_task_report() does + with string — needs str(task["id"])	AI	High
14:41	Function — Complete task	Works correctly: returns True, pending count dropped from 2 → 1	AI	
14:44	Function — Double complete BUG: Completing an already-completed task returns True — should return False. Allows marking same task done repeatedly	AI	Medium
14:45	Function — Invalid ID  Works correctly: Completing non-existent task 999 returns False — no crash, proper handling	AI	
14:47	Data — Blank title BUG: Task with completely empty title '' saved successfully — should be rejected or validated	Self	Medium
14:48	Function — Find by title	Works perfectly: Found exact match — returns full task object with all fields	Self	—
14:49	Function — Average priority	Calculates correctly: 1.0 — matches priority values of all tasks	Self	—
14:51	Function — Remove task	BUG: remove_task() returns None instead of True/False, and task is NOT removed — still shows 2 tasks	Self	High
14:53	Function — Remove invalid ID	BUG: Removing non-existent task 999 also returns None — function never removes anything and gives no clear feedback	Self	High

## BUG SUMMARY:

Bug ID	Description	Severity	Source
B-01	format_task_report() crashes — int vs str concatenation	High	AI
B-02	Double-complete returns True — allows duplicate completion	Medium	AI
B-03	Empty title saves — no input validation	Medium	Self
B-04	remove_task() does nothing — returns None, no removal	High	Self

## Source Breakdown:

 Source	Bugs Found	Percentage
AI-suggested avenues	2 bugs	50%
Self-found / unprompted	2 bugs	50%
Total	4 bugs	100%