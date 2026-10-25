# Lab 9: Exploratory Testing — Session Report

**Student Name:** Miguel K. J. Keitseng
**Student ID:** 23018310
**Date:** 25 October 2026
**Duration:** 45 minutes

---

## 1. Charter Recap
- **Mission:** Discover edge cases, unexpected behaviour, and functional defects in the Task Manager CLI — covering task creation, state changes, persistence, and output formatting.
- **Scope:** Adding, completing, listing, finding, saving, and removing tasks; input validation, error handling, and cross-session persistence.
- **Approach:** Applied 5 AI-suggested test avenues based on the SFDPOT heuristic, plus independent exploration.

## 2. AI-Suggested Coverage & Results
| AI Idea (SFDPOT) | Explored? | Key Finding |
|---|---|---|
| **Data** — Boundary & edge values | Yes | Empty titles save without validation — missing input check |
| **Function** — State transitions |  Yes | Completing works, but re-completing same task incorrectly returns True |
| **Operations** — Save/load sequences | Yes | Persistence works, but save/load functions are in unexpected module (`tasks.py` not `storage.py`) |
| **Time** — Persistence across sessions | Yes | Missing file handled gracefully; data survives reloads correctly |
| **Structure/Platform** — Interface & output | Yes | CLI crashes when displaying tasks — type error in report formatting |

## 3. Bugs Found
| ID | Description | Severity | Source |
|---|---|---|---|
| B-01 | `format_task_report()` in `storage.py` crashes — attempts string concatenation with integer `task["id"]` without conversion | High | AI |
| B-02 | `complete_task()` allows marking already-completed task as done again — returns True instead of False | Medium | AI |
| B-03 | `add_task()` accepts empty/blank title string — no validation to reject or prompt correction | Medium | Self |
| B-04 | `remove_task()` completely non-functional — returns `None` for both valid and invalid IDs, no task is actually removed | High | Self |

## 4. Source Breakdown
| Category | Bug Count | Percentage |
|---|---|---|
| AI-suggested avenues | 2 | 50% |
| Self-found / unprompted | 2 | 50% |
| **Total bugs identified** | **4** | **100%** |

## 5. Reflection
AI-suggested charters directly led to **2 critical findings**: the CLI display crash and the double-completion logic error. These were structural and behavioural issues I would likely have discovered eventually, but the SFDPOT framework focused my attention systematically and found them earlier in the session. My own independent exploration uncovered **equally significant defects**: the missing title validation and the completely broken remove function. AI provided a strong organised starting framework, but following my own curiosity and edge-case instincts proved equally valuable — especially for functions like `remove_task` that were less obvious from the initial charter.

## 6. Conclusion
This session demonstrated that AI co-piloting is a powerful accelerator for exploratory testing: it suggests structured perspectives and heuristics that ensure broad coverage from the start. However, AI does not replace independent critical thinking — half the bugs found came from following my own hunches. The most effective approach combines both: **use AI to establish a solid foundation and coverage plan, then apply your own judgement to dig deeper and chase unexpected leads.**

---
