"""Task management core logic."""
import json
import os

TASKS_FILE = "tasks.json"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_load_tasks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_load_tasks__mutmut)
def load_tasks():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_orig():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_1():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(None):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_2():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(None, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_3():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, None, encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_4():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding=None) as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_5():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open("r", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_6():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_7():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", ) as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_8():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "XXrXX", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_9():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "R", encoding="utf-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_10():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="XXutf-8XX") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_11():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="UTF-8") as f:
            return json.load(f)
    return []


def x_load_tasks__mutmut_12():
    """Load tasks from disk, returning an empty list if no file exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(None)
    return []

mutants_x_load_tasks__mutmut['_mutmut_orig'] = x_load_tasks__mutmut_orig # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_1'] = x_load_tasks__mutmut_1 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_2'] = x_load_tasks__mutmut_2 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_3'] = x_load_tasks__mutmut_3 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_4'] = x_load_tasks__mutmut_4 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_5'] = x_load_tasks__mutmut_5 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_6'] = x_load_tasks__mutmut_6 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_7'] = x_load_tasks__mutmut_7 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_8'] = x_load_tasks__mutmut_8 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_9'] = x_load_tasks__mutmut_9 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_10'] = x_load_tasks__mutmut_10 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_11'] = x_load_tasks__mutmut_11 # type: ignore # mutmut generated
mutants_x_load_tasks__mutmut['x_load_tasks__mutmut_12'] = x_load_tasks__mutmut_12 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_save_tasks__mutmut)
def save_tasks(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_orig(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_1(tasks):
    """Persist tasks to disk."""
    with open(None, "w") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_2(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, None) as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_3(tasks):
    """Persist tasks to disk."""
    with open("w") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_4(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, ) as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_5(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "XXwXX") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_6(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "W") as f:
        json.dump(tasks, f)


def x_save_tasks__mutmut_7(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(None, f)


def x_save_tasks__mutmut_8(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, None)


def x_save_tasks__mutmut_9(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(f)


def x_save_tasks__mutmut_10(tasks):
    """Persist tasks to disk."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, )

mutants_x_save_tasks__mutmut['_mutmut_orig'] = x_save_tasks__mutmut_orig # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_1'] = x_save_tasks__mutmut_1 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_2'] = x_save_tasks__mutmut_2 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_3'] = x_save_tasks__mutmut_3 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_4'] = x_save_tasks__mutmut_4 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_5'] = x_save_tasks__mutmut_5 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_6'] = x_save_tasks__mutmut_6 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_7'] = x_save_tasks__mutmut_7 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_8'] = x_save_tasks__mutmut_8 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_9'] = x_save_tasks__mutmut_9 # type: ignore # mutmut generated
mutants_x_save_tasks__mutmut['x_save_tasks__mutmut_10'] = x_save_tasks__mutmut_10 # type: ignore # mutmut generated
mutants_x_add_task__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_add_task__mutmut)
def add_task(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_orig(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_1(tasks, title, priority=2, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_2(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is not None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_3(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = None
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_4(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = None
    tasks.append(task)
    return task


def x_add_task__mutmut_5(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "XXidXX": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_6(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "ID": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_7(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) - 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_8(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 2,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_9(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "XXtitleXX": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_10(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "TITLE": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_11(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "XXpriorityXX": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_12(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "PRIORITY": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_13(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "XXtagsXX": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_14(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "TAGS": tags,
        "done": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_15(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "XXdoneXX": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_16(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "DONE": False,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_17(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": True,
    }
    tasks.append(task)
    return task


def x_add_task__mutmut_18(tasks, title, priority=1, tags=None):
    """Create a new task and append it to the task list."""
    if tags is None:
        tags = []
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "tags": tags,
        "done": False,
    }
    tasks.append(None)
    return task

mutants_x_add_task__mutmut['_mutmut_orig'] = x_add_task__mutmut_orig # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_1'] = x_add_task__mutmut_1 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_2'] = x_add_task__mutmut_2 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_3'] = x_add_task__mutmut_3 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_4'] = x_add_task__mutmut_4 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_5'] = x_add_task__mutmut_5 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_6'] = x_add_task__mutmut_6 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_7'] = x_add_task__mutmut_7 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_8'] = x_add_task__mutmut_8 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_9'] = x_add_task__mutmut_9 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_10'] = x_add_task__mutmut_10 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_11'] = x_add_task__mutmut_11 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_12'] = x_add_task__mutmut_12 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_13'] = x_add_task__mutmut_13 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_14'] = x_add_task__mutmut_14 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_15'] = x_add_task__mutmut_15 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_16'] = x_add_task__mutmut_16 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_17'] = x_add_task__mutmut_17 # type: ignore # mutmut generated
mutants_x_add_task__mutmut['x_add_task__mutmut_18'] = x_add_task__mutmut_18 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_complete_task__mutmut)
def complete_task(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def x_complete_task__mutmut_orig(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def x_complete_task__mutmut_1(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["XXidXX"] == task_id:
            task["done"] = True
            return True
    return False


def x_complete_task__mutmut_2(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["ID"] == task_id:
            task["done"] = True
            return True
    return False


def x_complete_task__mutmut_3(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] != task_id:
            task["done"] = True
            return True
    return False


def x_complete_task__mutmut_4(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = None
            return True
    return False


def x_complete_task__mutmut_5(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["XXdoneXX"] = True
            return True
    return False


def x_complete_task__mutmut_6(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["DONE"] = True
            return True
    return False


def x_complete_task__mutmut_7(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = False
            return True
    return False


def x_complete_task__mutmut_8(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return False
    return False


def x_complete_task__mutmut_9(tasks, task_id):
    """Mark a task as done by id."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return True

mutants_x_complete_task__mutmut['_mutmut_orig'] = x_complete_task__mutmut_orig # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_1'] = x_complete_task__mutmut_1 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_2'] = x_complete_task__mutmut_2 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_3'] = x_complete_task__mutmut_3 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_4'] = x_complete_task__mutmut_4 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_5'] = x_complete_task__mutmut_5 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_6'] = x_complete_task__mutmut_6 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_7'] = x_complete_task__mutmut_7 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_8'] = x_complete_task__mutmut_8 # type: ignore # mutmut generated
mutants_x_complete_task__mutmut['x_complete_task__mutmut_9'] = x_complete_task__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_pending_tasks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_pending_tasks__mutmut)
def get_pending_tasks(tasks):
    """Return all tasks that are not yet done."""
    return [task for task in tasks if not task["done"]]


def x_get_pending_tasks__mutmut_orig(tasks):
    """Return all tasks that are not yet done."""
    return [task for task in tasks if not task["done"]]


def x_get_pending_tasks__mutmut_1(tasks):
    """Return all tasks that are not yet done."""
    return [task for task in tasks if task["done"]]


def x_get_pending_tasks__mutmut_2(tasks):
    """Return all tasks that are not yet done."""
    return [task for task in tasks if not task["XXdoneXX"]]


def x_get_pending_tasks__mutmut_3(tasks):
    """Return all tasks that are not yet done."""
    return [task for task in tasks if not task["DONE"]]

mutants_x_get_pending_tasks__mutmut['_mutmut_orig'] = x_get_pending_tasks__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_pending_tasks__mutmut['x_get_pending_tasks__mutmut_1'] = x_get_pending_tasks__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_pending_tasks__mutmut['x_get_pending_tasks__mutmut_2'] = x_get_pending_tasks__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_pending_tasks__mutmut['x_get_pending_tasks__mutmut_3'] = x_get_pending_tasks__mutmut_3 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_average_priority__mutmut)
def average_priority(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_orig(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_1(tasks):
    """Return the average priority across all tasks."""
    if tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_2(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 1
    total = 0
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_3(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = None
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_4(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 1
    for task in tasks:
        total += task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_5(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total = task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_6(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total -= task["priority"]
    return total / len(tasks)


def x_average_priority__mutmut_7(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["XXpriorityXX"]
    return total / len(tasks)


def x_average_priority__mutmut_8(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["PRIORITY"]
    return total / len(tasks)


def x_average_priority__mutmut_9(tasks):
    """Return the average priority across all tasks."""
    if not tasks:
        return 0
    total = 0
    for task in tasks:
        total += task["priority"]
    return total * len(tasks)

mutants_x_average_priority__mutmut['_mutmut_orig'] = x_average_priority__mutmut_orig # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_1'] = x_average_priority__mutmut_1 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_2'] = x_average_priority__mutmut_2 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_3'] = x_average_priority__mutmut_3 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_4'] = x_average_priority__mutmut_4 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_5'] = x_average_priority__mutmut_5 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_6'] = x_average_priority__mutmut_6 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_7'] = x_average_priority__mutmut_7 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_8'] = x_average_priority__mutmut_8 # type: ignore # mutmut generated
mutants_x_average_priority__mutmut['x_average_priority__mutmut_9'] = x_average_priority__mutmut_9 # type: ignore # mutmut generated
mutants_x_find_task_by_title__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_task_by_title__mutmut)
def find_task_by_title(tasks, title):
    """Return the first task matching the given title."""
    for task in tasks:
        if task["title"] == title:
            return task


def x_find_task_by_title__mutmut_orig(tasks, title):
    """Return the first task matching the given title."""
    for task in tasks:
        if task["title"] == title:
            return task


def x_find_task_by_title__mutmut_1(tasks, title):
    """Return the first task matching the given title."""
    for task in tasks:
        if task["XXtitleXX"] == title:
            return task


def x_find_task_by_title__mutmut_2(tasks, title):
    """Return the first task matching the given title."""
    for task in tasks:
        if task["TITLE"] == title:
            return task


def x_find_task_by_title__mutmut_3(tasks, title):
    """Return the first task matching the given title."""
    for task in tasks:
        if task["title"] != title:
            return task

mutants_x_find_task_by_title__mutmut['_mutmut_orig'] = x_find_task_by_title__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_task_by_title__mutmut['x_find_task_by_title__mutmut_1'] = x_find_task_by_title__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_task_by_title__mutmut['x_find_task_by_title__mutmut_2'] = x_find_task_by_title__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_task_by_title__mutmut['x_find_task_by_title__mutmut_3'] = x_find_task_by_title__mutmut_3 # type: ignore # mutmut generated
mutants_x_remove_task__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_remove_task__mutmut)
def remove_task(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_orig(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_1(tasks, task_id):
    """Remove a task by id."""
    for i in range(None):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_2(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["XXidXX"] == task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_3(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["ID"] == task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_4(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["id"] != task_id:
            del tasks[i]
            break


def x_remove_task__mutmut_5(tasks, task_id):
    """Remove a task by id."""
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            return

mutants_x_remove_task__mutmut['_mutmut_orig'] = x_remove_task__mutmut_orig # type: ignore # mutmut generated
mutants_x_remove_task__mutmut['x_remove_task__mutmut_1'] = x_remove_task__mutmut_1 # type: ignore # mutmut generated
mutants_x_remove_task__mutmut['x_remove_task__mutmut_2'] = x_remove_task__mutmut_2 # type: ignore # mutmut generated
mutants_x_remove_task__mutmut['x_remove_task__mutmut_3'] = x_remove_task__mutmut_3 # type: ignore # mutmut generated
mutants_x_remove_task__mutmut['x_remove_task__mutmut_4'] = x_remove_task__mutmut_4 # type: ignore # mutmut generated
mutants_x_remove_task__mutmut['x_remove_task__mutmut_5'] = x_remove_task__mutmut_5 # type: ignore # mutmut generated
mutants_x_calculate_discount__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_discount__mutmut)
def calculate_discount(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == True:
        return price * 0.8
    else:
        return price


def x_calculate_discount__mutmut_orig(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == True:
        return price * 0.8
    else:
        return price


def x_calculate_discount__mutmut_1(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium != True:
        return price * 0.8
    else:
        return price


def x_calculate_discount__mutmut_2(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == False:
        return price * 0.8
    else:
        return price


def x_calculate_discount__mutmut_3(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == True:
        return price / 0.8
    else:
        return price


def x_calculate_discount__mutmut_4(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == True:
        return price * 1.8
    else:
        return price

mutants_x_calculate_discount__mutmut['_mutmut_orig'] = x_calculate_discount__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_discount__mutmut['x_calculate_discount__mutmut_1'] = x_calculate_discount__mutmut_1 # type: ignore # mutmut generated
mutants_x_calculate_discount__mutmut['x_calculate_discount__mutmut_2'] = x_calculate_discount__mutmut_2 # type: ignore # mutmut generated
mutants_x_calculate_discount__mutmut['x_calculate_discount__mutmut_3'] = x_calculate_discount__mutmut_3 # type: ignore # mutmut generated
mutants_x_calculate_discount__mutmut['x_calculate_discount__mutmut_4'] = x_calculate_discount__mutmut_4 # type: ignore # mutmut generated
