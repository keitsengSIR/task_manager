# Lab 5: Test Automation Framework & Self-Healing Locators

Student ID: 23018310
Course: COMP 441 Software Analysis and Testing

## What was completed
- Page Object Model (`ui_tests/task_page.py`) for a small Flask Task Manager page (`webapp/app.py`)
- Five data-driven Selenium + pytest tests reading `ui_tests/test_data.csv`
- Healenium (Docker, self-hosted) set up as a proxy on port 8085
- Intentional locator drift: button id `add-task-btn` -> `add-task-button` (set with `LOCATOR_DRIFT=1`)
- Runs without and with Healenium, with screenshots (see `screenshots/`)
- Report with results tables, analysis and reflection: `Lab5_Report.md`

## How to run
```powershell
pip install -r ui_tests\requirements-ui.txt
python -m webapp.app                                  # terminal 1, from task_manager
cd ui_tests; pytest -v                                # terminal 2 (local Chrome)

# through Healenium (stack running from the cloned healenium repo)
$env:HEALENIUM_URL="http://localhost:8085"
$env:BASE_URL="http://host.docker.internal:5000"
pytest -v

# drift: restart the app with $env:LOCATOR_DRIFT="1"
```

## Notes
- The web app was written for this lab because the sample Task Manager repo is a command-line program.
- Page Object waits for the form-submit reload after clicking Add Task (fixes a stale-element race).
