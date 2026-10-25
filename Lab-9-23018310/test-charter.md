# Test Charter — Lab 9

**Application:** Task Manager (Python CLI)
**Feature:** Core Task Management Functionality
**Date:** 25 October 2026
**Tester:** Miguel K. J. Keitseng
**Timebox:** 45 minutes

## Mission
Discover unexpected behaviour, edge cases, and usability issues in the task creation, storage, and reporting features — using both my own intuition and AI-suggested test approaches.

## Scope — What to Cover
- Adding tasks (valid and invalid inputs)
- Marking tasks as complete
- Filtering pending tasks
- Loading/saving from storage
- Edge cases: empty lists, duplicate titles, boundary values

## Out of Scope
- CLI styling / cosmetic changes (covered in Lab 8)
- Third-party library bugs
- Refactoring or code improvements

## Test Techniques to Use
- Boundary value analysis
- Error guessing
- SFDPOT heuristics (Structure, Function, Data, Platform, Operations, Time)