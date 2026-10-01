# COMP 441 Lab 2: Static Analysis (Metrics, Linting & AI Code Review)

Tools: pylint 4.1.1, radon, Claude (AI assistant). Target: `app/` in the Task Manager repo.
Commands: `pylint app/ > lint_report_before.txt`, `radon cc -s app/`, `radon mi -s app/`.

## 1. Linter summary

- Before fixes: 12 messages, score **8.33/10** (`lint_report_before.txt`)
- After fixes: 8 messages, score **8.92/10** (`lint_report_after.txt`)

Notably, pylint did not report the SQL injection (D02), the str + int crash (D03), the off-by-one (D04) or the divide-by-zero (D05) from Lab 1. It only reached the hard-coded API key indirectly, through the TODO comment.

## 2. Complexity (radon)

Five most complex functions (by cyclomatic complexity):

| Function | File | CC | Risk band |
|----------|------|----|-----------|
| complete_task | app/tasks.py | 3 | A |
| get_pending_tasks | app/tasks.py | 3 | A |
| find_task_by_title | app/tasks.py | 3 | A |
| remove_task | app/tasks.py | 3 | A |
| load_tasks | app/tasks.py | 2 | A |

Every function is in band A (CC 1 to 5), so there is no complexity hotspot. `load_tasks`, `average_priority`, `calculate_discount` and `format_task_report` all tie at CC 2, and `load_tasks` is listed as the fifth entry.

Maintainability index: cli.py 72.27 (A), storage.py 72.97 (A), tasks.py 45.51 (A, the lowest), `__init__.py` 100 (A). Full output is in `radon_report.txt`.

## 3. Triage of ten findings

| # | Pylint finding | Location | Severity | Fix effort |
|---|----------------|----------|----------|------------|
| 1 | W0511 fixme: TODO says to move the API key to an env var | storage.py:4 | Critical | Low |
| 2 | W0102 dangerous-default-value (`tags=[]`) | tasks.py:23 | High | Low |
| 3 | R1732 consider-using-with (file never closed) | tasks.py:11 | Medium | Low |
| 4 | R1710 inconsistent-return-statements | tasks.py:62 | Low | Low |
| 5 | W1514 unspecified-encoding | tasks.py:11 | Low | Low |
| 6 | W1514 unspecified-encoding | tasks.py:19 | Low | Low |
| 7 | W0611 unused-import (`save_tasks`) | cli.py:2 | Low | Low |
| 8 | W0611 unused-import (`add_task`) | cli.py:2 | Low | Low |
| 9 | C0121 singleton-comparison (`== True`) | tasks.py:79 | Low | Low |
| 10 | C0200 consider-using-enumerate | tasks.py:71 | Low | Low |

Not triaged (remaining two): R1705 no-else-return (tasks.py:79) and C0116 missing docstring (cli.py:6).

## 4. Three fixes (`lab2_fixes.patch`)

1. **#1 Hard-coded API key** (storage.py): replaced the literal with `os.environ.get("TASK_MANAGER_API_KEY")`.
2. **#2 Mutable default** (tasks.py): changed `tags=[]` to `tags=None` and create a fresh list inside the function.
3. **#3 Unclosed file** (tasks.py): wrapped the file read in `with open(..., encoding="utf-8")`. This also resolved finding #5 (the encoding warning on line 11).

Re-running pylint confirmed all three are gone (messages dropped from 12 to 8, score 8.33 to 8.92). `pytest` still shows 4 passed and 2 failed, since the two failing tests cover Lab 1 defects D04 and D05, which these fixes do not touch.

Apply the patch with `git apply lab2_fixes.patch`.

## 5. AI code review vs. linter

Two originally flagged snippets were given to the AI assistant for a code review: `add_task` (tasks.py:23-33) and `load_tasks` (tasks.py:8-14).

| Snippet | Caught by pylint | Caught by AI review | Caught only by AI | Caught only by pylint |
|---------|------------------|---------------------|-------------------|-----------------------|
| add_task | Dangerous default `tags=[]` | Same default-argument bug, explained as tags being shared between all tasks | `id = len(tasks) + 1` gives duplicate IDs after a removal; no validation of title or priority; function both mutates its input and returns | Nothing unique |
| load_tasks | File not closed with `with`; no explicit encoding | Unclosed file | No handling of corrupt or empty JSON; relative path depends on the working directory; the `exists` check followed by `open` is a race | Missing encoding (not mentioned by the AI) |

## 6. Reflection

The AI reviewer raised several categories that pylint structurally cannot detect. Pylint matches known patterns in the syntax tree, so it cannot reason about what a function is meant to do. The AI noticed that `add_task` generates duplicate IDs once a task has been removed, that nothing validates the priority, and that `load_tasks` would crash on a corrupt file. Those are logic, design and robustness issues, and they depend on intent. In the other direction, the linter was more systematic. It reported a precise, repeatable encoding warning that the AI did not mention. So the two are complementary: the linter gives consistent coverage of known rules, while the AI gives broader judgement that needs a human to verify it.