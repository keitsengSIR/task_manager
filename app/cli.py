"""Command-line entry point for the Task Manager sample app."""
from app.tasks import load_tasks, save_tasks, add_task, get_pending_tasks
from app.storage import format_task_report

def main():
    tasks = load_tasks()
    # YOUR DELIBERATE CHANGE — different header & spacing
    print("=" * 50)
    print("      ✅ TASK MANAGER — SYSTEM STATUS ✅")
    print("=" * 50)
    print()  # extra blank line
    print("Loaded", len(tasks), "tasks")
    print()
    print(format_task_report(tasks))
    print()
    pending = get_pending_tasks(tasks)
    print("▶ Pending tasks:", len(pending))

if __name__ == "__main__":
    main()