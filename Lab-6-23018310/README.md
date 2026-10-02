# Lab 6 — AI-Generated Test Cases & Coverage Delta
**Student ID:** 23018310
**Module:** COMP 441 Software Analysis and Testing
**Date:** 2 October 2026

## Overview
This lab compares **AI-generated** and **manually written** unit tests for three previously untested functions in `app/tasks.py`:

| Function | Purpose |
|---|---|
| `load_tasks()` | Load tasks from disk; return empty list if no file exists |
| `save_tasks()` | Write task list to JSON file |
| `find_task_by_title()` | Find first task by title; return `None` if not found |

