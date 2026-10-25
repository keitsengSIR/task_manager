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
import os

# ===== load_tasks & save_tasks =====
def test_save_creates_file():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    tasks = [{"title": "AI Test", "done": True}]
    save_tasks(tasks)
    assert os.path.isfile("tasks.json")

def test_load_returns_list():
    result = load_tasks()
    assert isinstance(result, list)

# ===== find_task_by_title =====
def test_find_returns_correct_task():
    tasks = [{"title": "One"}, {"title": "Two"}]
    found = find_task_by_title(tasks, "One")
    assert found["title"] == "One"

def test_find_returns_none_when_absent():
    tasks = [{"title": "Report"}]
    assert find_task_by_title(tasks, "Missing") is None

# ===== add_task =====
def test_add_assigns_incrementing_ids():
    tasks = []
    t1 = add_task(tasks, "First")
    t2 = add_task(tasks, "Second")
    assert t1["id"] == 1
    assert t2["id"] == 2

def test_add_with_custom_priority_and_tags():
    tasks = []
    task = add_task(tasks, "Tagged", priority=5, tags=["urgent"])
    assert task["priority"] == 5
    assert task["tags"] == ["urgent"]

# ===== complete_task =====
def test_complete_returns_true_on_success():
    tasks = []
    t = add_task(tasks, "Go")
    assert complete_task(tasks, t["id"]) is True

def test_complete_invalid_id_returns_false():
    tasks = []
    add_task(tasks, "No")
    assert complete_task(tasks, -1) is False

# ===== get_pending_tasks =====
def test_pending_all_when_none_done():
    tasks = []
    add_task(tasks, "P1")
    add_task(tasks, "P2")
    assert len(get_pending_tasks(tasks)) == 2

def test_pending_none_when_all_done():
    tasks = []
    t1 = add_task(tasks, "D1")
    t2 = add_task(tasks, "D2")
    complete_task(tasks, t1["id"])
    complete_task(tasks, t2["id"])
    assert len(get_pending_tasks(tasks)) == 0

# ===== average_priority =====
def test_average_single_task():
    tasks = [{"title": "Solo", "priority": 5}]
    assert average_priority(tasks) == 5.0

def test_average_mixed_values():
    tasks = [
        {"title": "L", "priority": 1},
        {"title": "M", "priority": 3},
        {"title": "H", "priority": 5},
    ]
    assert average_priority(tasks) == 3.0

# ===== remove_task =====
def test_remove_reduces_length():
    tasks = []
    add_task(tasks, "A")
    t2 = add_task(tasks, "B")
    initial = len(tasks)
    remove_task(tasks, t2["id"])
    assert len(tasks) == initial - 1

def test_remove_first_item():
    tasks = []
    t1 = add_task(tasks, "First")
    add_task(tasks, "Second")
    remove_task(tasks, t1["id"])
    assert tasks[0]["title"] == "Second"

# ===== calculate_discount =====
def test_discount_premium_large_amount():
    assert calculate_discount(2000, is_premium=True) == 1600.0

def test_discount_not_premium_large_amount():
    assert calculate_discount(2000, is_premium=False) == 2000.0

def test_discount_zero_amount_premium():
    assert calculate_discount(0, is_premium=True) == 0.0
