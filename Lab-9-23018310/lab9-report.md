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

This session demonstrated that AI co-piloting serves as a powerful accelerator for exploratory testing: it provides structured perspectives and established heuristics that ensure broad, systematic coverage from the very start. AI guided me to critical issues — such as the type mismatch in the report formatter and the duplicate-completion logic — that set a strong foundation for the session.
However, AI does not replace independent critical thinking. Exactly half of the bugs identified came from following my own curiosity and instincts — including the missing input validation and the completely broken removal function. These issues would have remained hidden if I had relied on AI suggestions alone.
The most effective approach combines both: use AI to establish a solid framework and ensure comprehensive coverage, then apply your own judgement to dig deeper, question assumptions, and chase unexpected leads. Together, AI guidance and human curiosity produce more thorough testing than either could achieve alone.
