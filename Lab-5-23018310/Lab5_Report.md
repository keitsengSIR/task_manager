# COMP 441 Lab 5: Test Automation Framework & Self-Healing Locators

Student ID: 23018310

**Tools:** Python, Selenium, pytest, Healenium (Docker, self-hosted proxy), Flask sample web app.

## 1. Setup

The sample Task Manager repo is a command-line program, so a small Flask web page (`webapp/app.py`) was added as the application under test. It has a title box, a priority dropdown, an **Add Task** button, an error message area and a task list. Selenium was chosen because Healenium works as a proxy for Selenium.

Screenshot 5-01 (install): `screenshots/shot-5-01-install.png`
Screenshot 5-02 (Page Object): `screenshots/shot-5-02-page-object.png`
Screenshot 5-03 (app running): `screenshots/shot-5-03-app-running.png`

## 2. Page Object and data-driven tests

`ui_tests/task_page.py` holds the locators (`task-title`, `task-priority`, `add-task-btn`, `error-message`, `#task-list .task-item`) and the actions (`open`, `add_task`, `task_texts`, `error_text`). `ui_tests/test_task_ui.py` reads `test_data.csv` and creates one test per row.

| Test | Title | Priority | Expected | Result (local, no drift) |
|---|---|---|---|---|
| UI01 | Write report | 1 | Task added | |
| UI02 | Buy groceries | 3 | Task added | |
| UI03 | Prepare COMP 441 presentation slides | 5 | Task added | |
| UI04 | Review pull request | 4 | Task added | |
| UI05 | (empty) | 2 | Error "Title is required" | |

Screenshot 5-04: `screenshots/shot-5-04-5-pass-local.png`

## 3. Healenium setup

Healenium was started from the cloned healenium repository with Docker Compose (proxy on port 8085, backend on port 7878). Only the Chrome node was needed for the tests.

Screenshot 5-05 (docker ps): `screenshots/shot-5-05-docker-ps.png`
Screenshot 5-06 (empty dashboard): `screenshots/shot-5-06-empty-dashboard.png`

**Baseline through the proxy (no drift):** 5 passed in 30.69 s. Healenium needs this run so it has seen the working locator.

Screenshot 5-07: `screenshots/shot-5-07-baseline-proxy.png`

## 4. Locator drift, without Healenium

The app was restarted with `LOCATOR_DRIFT=1`, which renames the button id from `add-task-btn` to `add-task-button`. The Page Object was not changed.

| Test | Result without Healenium | Reason |
|---|---|---|
| UI01 to UI04 | Failed | `TimeoutException` at `task_page.py:36`, waiting for the button by `add-task-btn` |
| UI05 | Failed | Same timeout at the same line |

Overall: 5 failed in 98.54 s.

Screenshot 5-08: `screenshots/shot-5-08-failures-no-healenium.png`

## 5. With Healenium

The same suite, with the drifted app still running, through the Healenium proxy: 5 passed in 64.10 s.

Screenshot 5-09: `screenshots/shot-5-09-results-with-healenium.png`
Screenshot 5-10 (healing report): `screenshots/shot-5-10-healing-report.png`

| Item | Result |
|---|---|
| Tests that failed without Healenium | 5 |
| Tests that passed with Healenium | 5 |
| Healing success rate (healed / broken locators) | *(fill in: 1 distinct locator broken; say how you counted)* |
| New locator Healenium chose for the button | *(read from the report)* |
| Was the healed element correct? | *(check it points at the Add Task button)* |
| Cases where it chose the wrong element | *(read from the report)* |

## 6. Analysis (write this yourself)

In my report, Healenium replaced the locator  with [id="add-task-btn"] and gave it a score of 0.97.
This shows it picked the element by tag name plus the new id.
The healed element was / was not the correct one because The healed locator can only match one thing. button#add-task-button means a <button> with that id. Your page has one button, the Add Task button, and the drift only renamed its id. Nothing else on the page can match that selector.The tests only passed if the click did the right thing. Each test clicked the healed element and then checked the outcome. UI01 to UI04 asserted that the new task appeared in the list, and UI05 asserted that the "Title is required" error appeared. Neither would have happened if Healenium had clicked a different element.
The healed element was / was not the correct one because The healed locator can only match one thing. button#add-task-button means a <button> with that id. Your page has one button, the Add Task button, and the drift only renamed its id. Nothing else on the page can match that selector.The tests only passed if the click did the right thing. Each test clicked the healed element and then checked the outcome. UI01 to UI04 asserted that the new task appeared in the list, and UI05 asserted that the "Title is required" error appeared. Neither would have happened if Healenium had clicked a different element.The report can confirm it by eye. The Screenshot column in the healing entry highlights the element Healenium chose. If it shows the Add Task button, that is direct evidence. Look at it before you write the sentence, and don't rely on my reasoning alone.
The runs took about 31 s (baseline), 98 s (timeouts) and 64 s (healing).

## 7. Reflection 


