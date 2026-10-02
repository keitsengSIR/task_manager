"""Tiny Flask front-end for the Task Manager (the 'application under test' for Lab 5).

Run from the task_manager folder:   python -m webapp.app
Locator drift (Lab 5, step 6):      $env:LOCATOR_DRIFT="1"; python -m webapp.app
"""
import os
from flask import Flask, render_template_string, request

app = Flask(__name__)
TASKS = []  # in-memory list, enough for the lab

# Normal build: the button id is "add-task-btn".
# Drifted build: the developer "renamed" it to "add-task-button" (simulated DOM drift).
DRIFT = os.environ.get("LOCATOR_DRIFT") == "1"
BUTTON_ID = "add-task-button" if DRIFT else "add-task-btn"

PAGE = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Task Manager</title>
<style>
 body{font-family:Arial,sans-serif;max-width:560px;margin:40px auto;}
 .error{color:#b00020;margin:8px 0;}
 .task-item{padding:4px 0;}
 .btn{padding:6px 14px;background:#1565c0;color:#fff;border:0;border-radius:4px;}
</style></head>
<body>
 <h1>Task Manager</h1>
 <form method="post" action="/" novalidate>
  <label for="task-title">Title</label>
  <input type="text" id="task-title" name="title" placeholder="Task title">
  <label for="task-priority">Priority</label>
  <select id="task-priority" name="priority">
   {% for p in range(1, 6) %}<option value="{{ p }}">{{ p }}</option>{% endfor %}
  </select>
  <button type="submit" id="{{ button_id }}" class="btn" name="add">Add Task</button>
 </form>
 <div id="error-message" class="error">{{ error }}</div>
 <h2>Tasks</h2>
 <ul id="task-list">
  {% for t in tasks %}<li class="task-item">{{ t.title }} (priority {{ t.priority }})</li>{% endfor %}
 </ul>
</body></html>"""


@app.route("/", methods=["GET", "POST"])
def index():
    error = ""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "1")
        if not title:
            error = "Title is required"
        else:
            TASKS.append({"title": title, "priority": priority})
    return render_template_string(PAGE, tasks=TASKS, error=error, button_id=BUTTON_ID)


if __name__ == "__main__":
    # host 0.0.0.0 so the Docker browser can reach it via host.docker.internal
    app.run(host="0.0.0.0", port=5000, debug=False)
