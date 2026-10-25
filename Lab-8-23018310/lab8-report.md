# Lab 8: Visual Regression & Accessibility Testing

**Student Name:** Miguel K. J. Keitseng
**Student ID:** 23018310
**Module:** COMP 441 Software Analysis and Testing
**Date:** 25 October 2026

---

## 1. Introduction

This lab applied two complementary testing approaches to a command-line task management application: **visual regression testing** to detect deliberate and unintended interface changes, and **accessibility evaluation** to ensure output is clear and usable for all users, including those relying on assistive technologies. The objectives were to establish a visual baseline, introduce a deliberate formatting change, assess accessibility, implement improvements, and explain why both testing methods are necessary.

## 2. Tools & Context

The system under test is a Python command-line interface (CLI). Visual regression and accessibility focus on text formatting, structure, and clarity rather than web styling.

| Method | Purpose |
|---|---|
| Terminal output comparison | Baseline vs updated visual inspection |
| Manual structure review | Accessibility assessment for screen-reader compatibility |
| Python code modification | Applied deliberate formatting changes |

## 3. Visual Regression Testing

### 3.1 Baseline Established

Original unmodified output:

```text
Loaded 0 tasks

Pending tasks: 0
```

![!\[alt text\](<Screenshot 2026-10-25 133918.png>)](screenshots/lab8-baseline.png)

### 3.2 Deliberate Change Applied

File `app/cli.py` was updated to improve formatting.

**Before:**

```python
def main():
    tasks = load_tasks()
    print("Loaded", len(tasks), "tasks")
    print(format_task_report(tasks))
    pending = get_pending_tasks(tasks)
    print("Pending tasks:", len(pending))
```

**After:**

```python
def main():
    tasks = load_tasks()
    print("=" * 50)
    print("      ✅ TASK MANAGER — SYSTEM STATUS ✅")
    print("=" * 50)
    print()
    print("Loaded", len(tasks), "tasks")
    print()
    report = format_task_report(tasks)
    if report:
        print(report)
    else:
        print("No tasks currently stored.")
    print()
    pending = get_pending_tasks(tasks)
    print("▶ Pending tasks:", len(pending))
```

### 3.3 Updated Output & Difference

```text
==================================================
      ✅ TASK MANAGER — SYSTEM STATUS ✅
==================================================

Loaded 0 tasks

No tasks currently stored.

▶ Pending tasks: 0
```
![!\[alt text\](<Screenshot 2026-10-25 134022.png>)](screenshots/lab8-diff.png)

**Changes observed:**

- New header with border lines and descriptive title
- ~25% more vertical spacing between sections
- Visual symbols added alongside text labels
- Clear message displayed when no tasks exist

---

## 4. Accessibility Evaluation & Remediation

### 4.1 Initial Assessment

For CLI applications, accessibility means predictable structure, unambiguous labels, and independence from colour or visual-only cues. The original output functioned but could be clearer:

| Check Area | Finding |
|---|---|
| Empty state clarity | "Loaded 0 tasks" did not explicitly confirm expected behaviour |
| Label structure | Functional but lacked visual hierarchy |

### 4.2 Fix 1 — Clear Empty State Message

**Issue:** Users could misinterpret "0 tasks" as a loading failure rather than an empty but valid state.

**Resolution:** Added explicit confirmation:

```text
No tasks currently stored.
```

**Impact:** All users, including those using screen readers, receive unambiguous confirmation that the system is working correctly.

### 4.3 Fix 2 — Symbols as Enhancement, Not Replacement

**Issue:** Visual indicators can confuse assistive technology if they stand alone.

**Resolution:** Symbols (✅, ▶) were placed alongside full descriptive text:

```text
      ✅ TASK MANAGER — SYSTEM STATUS ✅
▶ Pending tasks: 0
```

**Impact:** Sighted users get quick visual cues; assistive technology reads the text labels so no information is lost. This follows WCAG guidance on not relying on sensory characteristics alone.

### 4.4 Verification

| Check | Result |
|---|---|
| All information available as text | ✅ Pass |
| Empty state unambiguous | ✅ Pass |
| Consistent structure | ✅ Pass — Header → Summary → Detail |
| No colour-only cues used | ✅ Pass — works on any terminal theme |

---

## 5. Reflection & Discussion

### 5.1 What Visual Testing Cannot Catch

Pixel-difference and visual inspection tests cannot detect:

- **Ambiguity:** output looks complete but leaves room for misinterpretation
- **Missing confirmation:** zero counts without explicit context
- **Symbol-only meaning:** icons render fine but lack text alternatives
- **Label clarity:** phrasing that is technically correct but confusing to new users

These are invisible to visual testing because they do not alter appearance. They affect how output is understood.

### 5.2 Why Both Test Types Are Necessary

| Approach | Detects | Limitation |
|---|---|---|
| Visual Regression | Layout shifts, formatting changes, unintended modifications | Cannot assess whether output is understandable or inclusive |
| Accessibility Review | Clarity, structure, assistive-technology compatibility | Cannot catch unintended styling or layout changes |

Running both ensures the interface looks correct and works correctly for everyone.

---

## 6. Conclusion

This lab demonstrated that visual consistency does not guarantee inclusive quality. The deliberate formatting change was clearly detectable as a visual difference, and the accessibility review identified opportunities to make output clearer and more inclusive.

The key takeaway: visual checks alone are never enough. Automated visual testing catches appearance regressions; accessibility review ensures the experience is usable by all. Combining both produces software that looks good and works well for every user.