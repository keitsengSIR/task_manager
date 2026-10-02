"""Five data-driven UI tests. Data comes from test_data.csv, not hard-coded."""
import csv
import pathlib
import pytest
from task_page import TaskPage

DATA_FILE = pathlib.Path(__file__).with_name("test_data.csv")


def load_rows():
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


ROWS = load_rows()


@pytest.mark.parametrize("row", ROWS, ids=[r["test_id"] for r in ROWS])
def test_add_task(driver, base_url, row):
    page = TaskPage(driver, base_url)
    page.open()
    page.add_task(row["title"], row["priority"])

    if row["expected_result"] == "added":
        # the new task must now appear in the list
        assert any(row["expected_text"] in t for t in page.task_texts())
    else:
        # invalid input: an error message must be shown
        assert page.error_text() == row["expected_text"]
