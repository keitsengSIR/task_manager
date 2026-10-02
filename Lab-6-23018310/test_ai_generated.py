"""AI-generated tests for load_tasks, save_tasks, find_task_by_title."""
import os
import json
import pytest
from app.tasks import load_tasks, save_tasks, find_task_by_title

# Override the tasks file path for tests
TEST_FILE = "test_tasks.json"

@pytest.fixture(autouse=True)
def isolate_test_file(monkeypatch):
    """Use a test-specific file and clean up after."""
    monkeypatch.setattr("app.tasks.TASKS_FILE", TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_load_tasks_returns_empty_list_when_no_file():
    """AI: Should return empty list if file doesn't exist."""
    result = load_tasks()
    assert result == []


def test_load_tasks_reads_saved_data():
    """AI: Should correctly load previously saved tasks."""
    data = [{"id": 1, "title": "Test", "done": False}]
    with open(TEST_FILE, "w") as f:
        json.dump(data, f)
    
    result = load_tasks()
    assert result == data
    assert len(result) == 1


def test_save_tasks_writes_readable_data():
    """AI: Saved data should be loadable back."""
    tasks = [{"id": 1, "title": "Saved Task", "done": False}]
    
    save_tasks(tasks)
    
    with open(TEST_FILE, "r") as f:
        loaded = json.load(f)
    assert loaded == tasks


def test_find_task_by_title_finds_match():
    """AI: Should return the task when title matches."""
    tasks = [
        {"id": 1, "title": "Buy milk", "done": False},
        {"id": 2, "title": "Do homework", "done": False},
    ]
    
    result = find_task_by_title(tasks, "Buy milk")
    assert result is not None
    assert result["id"] == 1


def test_find_task_by_title_returns_none_when_missing():
    """AI: Should return None if no task matches."""
    tasks = [{"id": 1, "title": "Existing", "done": False}]
    
    result = find_task_by_title(tasks, "Not There")
    assert result is None