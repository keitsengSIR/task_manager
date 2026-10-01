# COMP 441 Lab 1: Environment Setup & Manual Defect Hunting

**Student:** Miguel Keitseng (<studentID>)
**Repository:** https://github.com/keitsengSIR/task_manager

## What was completed

- Installed and verified the toolchain: Git 2.55.0, Python 3.14.3, pip 25.3 (see `tool-versions.png`).
- Cloned the sample Task Manager repository, installed dependencies and ran the application locally.
- Read the source files without running any tools and logged 16 suspected defects (see `lab-1-defect-log.md`). Each has an ID, file, line, description, severity and how it was found.
- Ran the existing test suite with `pytest`: 6 tests, 4 passed, 2 failed (`test_get_pending_tasks_includes_first_task` and `test_average_priority_of_empty_list`).
- Set up an AI assistant (Claude) and confirmed it can answer a question about the repository (see `ai-assistant-confirmation.png`).
- Wrote the reflection on which defects a linter or test would catch and which need manual reading (section 4 of the defect log).

## Files

- `lab-1-defect-log.md`: defect log, test results, tool versions and reflection
- `tool-versions.png`: Git, Python and pip versions
- `ai-assistant-confirmation.png`: AI assistant answering a question about the repo

## Notes

No source code was modified in this lab. Defects are logged only, to be addressed in later labs.