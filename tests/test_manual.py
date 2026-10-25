from app.tasks import (
    add_task,
    complete_task,
    get_pending_tasks,
    average_priority,
    calculate_discount,
    load_tasks,
    save_tasks,
    find_task_by_title,
    remove_task
)

# ===== load_tasks & save_tasks =====
def test_save_and_load_tasks():
    tasks = [{"title": "Study", "done": False, "priority": 2}]
    save_tasks(tasks)
    loaded = load_tasks()
    assert loaded == tasks

def test_load_tasks_returns_empty_when_no_file():
    import os
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    result = load_tasks()
    assert result == []  # covers line 13

# ===== find_task_by_title =====
def test_finds_existing_task():
    tasks = [{"title": "A"}, {"title": "B"}]
    found = find_task_by_title(tasks, "B")
    assert found is not None
    assert found["title"] == "B"

def test_returns_none_for_missing_task():
    tasks = [{"title": "A"}]
    assert find_task_by_title(tasks, "Z") is None

# ===== add_task =====
def test_add_task_increases_list():
    tasks = []
    add_task(tasks, "First")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "First"

def test_add_task_default_priority_and_tags():
    tasks = []
    task = add_task(tasks, "New")
    assert task["priority"] == 1
    assert task["tags"] == []  # covers default tags=None logic

# ===== complete_task =====
def test_complete_task_marks_by_id():
    tasks = []
    t1 = add_task(tasks, "Task 1")
    result = complete_task(tasks, t1["id"])
    assert result is True
    assert tasks[0]["done"] is True

def test_complete_task_bad_id_returns_false():
    tasks = []
    add_task(tasks, "Here")
    assert complete_task(tasks, 999) is False

# ===== get_pending_tasks =====
def test_pending_excludes_done():
    tasks = []
    t1 = add_task(tasks, "Pending")
    t2 = add_task(tasks, "Done")
    complete_task(tasks, t2["id"])
    pending = get_pending_tasks(tasks)
    assert len(pending) == 1
    assert pending[0]["id"] == t1["id"]

def test_pending_empty_when_all_done():
    tasks = []
    complete_task(tasks, add_task(tasks, "D1")["id"])
    complete_task(tasks, add_task(tasks, "D2")["id"])
    assert len(get_pending_tasks(tasks)) == 0

# ===== average_priority =====
def test_average_calculation():
    tasks = [
        {"title": "A", "priority": 2},
        {"title": "B", "priority": 4},
    ]
    assert average_priority(tasks) == 3.0

def test_average_empty_is_zero():
    assert average_priority([]) == 0  # covers line 54

# ===== remove_task — lines 70-73 =====
def test_remove_task_deletes_by_id():
    tasks = []
    t1 = add_task(tasks, "Keep")
    t2 = add_task(tasks, "Remove")
    remove_task(tasks, t2["id"])
    assert len(tasks) == 1
    assert tasks[0]["id"] == t1["id"]

def test_remove_task_not_found_does_nothing():
    tasks = [{"id": 1, "title": "Here"}]
    remove_task(tasks, 999)  # no return value, just doesn't crash
    assert len(tasks) == 1

# ===== calculate_discount =====
def test_discount_premium_gets_20_percent_off():
    assert calculate_discount(100, is_premium=True) == 80.0

def test_discount_not_premium_no_discount():
    assert calculate_discount(100, is_premium=False) == 100.0
