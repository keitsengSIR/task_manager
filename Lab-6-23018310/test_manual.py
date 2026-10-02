"""Manually written tests — no AI assistance."""
import os
import json
import pytest
from app.tasks import load_tasks, save_tasks, find_task_by_title

TEST_FILE = "manual_test_tasks.json"

@pytest.fixture(autouse=True)
def use_test_file(monkeypatch):
    monkeypatch.setattr("app.tasks.TASKS_FILE", TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_load_tasks_no_file_returns_empty():
    """Manual: Fresh start = empty list."""
    # Ensure file does not exist
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    tasks = load_tasks()
    assert tasks == []
    assert isinstance(tasks, list)


def test_load_tasks_existing_file_returns_contents():
    """Manual: Reads exactly what was written."""
    expected = [
        {"id": 1, "title": "First", "priority": 2, "done": False},
        {"id": 2, "title": "Second", "priority": 5, "done": True},
    ]
    
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        json.dump(expected, f)
    
    actual = load_tasks()
    assert actual == expected
    # Verify field integrity
    assert actual[0]["priority"] == 2
    assert actual[1]["done"] is True


def test_save_tasks_creates_file():
    """Manual: File exists after save."""
    tasks = [{"id": 1, "title": "New Task", "done": False}]
    
    save_tasks(tasks)
    
    assert os.path.exists(TEST_FILE)


def test_save_tasks_preserves_all_fields():
    """Manual: All keys/values survive round-trip."""
    original = {
        "id": 5,
        "title": "Full Data",
        "priority": 3,
        "tags": ["work", "urgent"],
        "done": False,
    }
    
    save_tasks([original])
    
    with open(TEST_FILE, "r") as f:
        loaded = json.load(f)
    
    assert loaded[0]["id"] == 5
    assert loaded[0]["title"] == "Full Data"
    assert loaded[0]["priority"] == 3
    assert loaded[0]["tags"] == ["work", "urgent"]
    assert loaded[0]["done"] is False


def test_find_task_by_title_exact_match():
    """Manual: Finds the correct task when titles match exactly."""
    tasks = [
        {"id": 1, "title": "Alpha", "done": False},
        {"id": 2, "title": "Beta", "done": False},
        {"id": 3, "title": "Gamma", "done": False},
    ]
    
    found = find_task_by_title(tasks, "Beta")
    assert found is not None
    assert found["id"] == 2
    assert found["title"] == "Beta"


def test_find_task_by_title_case_sensitive():
    """Manual: Title matching is case-sensitive."""
    tasks = [{"id": 1, "title": "Hello", "done": False}]
    
    found = find_task_by_title(tasks, "hello")
    assert found is None


def test_find_task_by_title_empty_list():
    """Manual: Returns None on empty list."""
    found = find_task_by_title([], "Anything")
    assert found is None