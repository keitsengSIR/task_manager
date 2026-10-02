"""Page Object for the Task Manager page.

All locators live here, in ONE place. If the UI changes, only this file changes.
Tests never call driver.find_element() themselves.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TaskPage:
    TITLE_INPUT = (By.ID, "task-title")
    PRIORITY_SELECT = (By.ID, "task-priority")
    ADD_BUTTON = (By.ID, "add-task-btn")          # <- the locator we break in step 6
    ERROR_MESSAGE = (By.ID, "error-message")
    TASK_ITEMS = (By.CSS_SELECTOR, "#task-list .task-item")

    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    # ---- actions -------------------------------------------------------
    def open(self):
        self.driver.get(self.base_url)
        self.wait.until(EC.visibility_of_element_located(self.TITLE_INPUT))

    def add_task(self, title, priority):
        title_box = self.wait.until(EC.visibility_of_element_located(self.TITLE_INPUT))
        title_box.clear()
        if title:
            title_box.send_keys(title)
        self.driver.find_element(*self.PRIORITY_SELECT).send_keys(str(priority))
        old_page = self.driver.find_element(By.TAG_NAME, "html")
        # If the button's id has changed, this line is where the test fails (or heals).
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        # Wait for the form submit to reload the page before anyone reads it.
        self.wait.until(EC.staleness_of(old_page))
        self.wait.until(EC.presence_of_element_located(self.TITLE_INPUT))

    # ---- queries -------------------------------------------------------
    def task_texts(self):
        return [e.text for e in self.driver.find_elements(*self.TASK_ITEMS)]

    def error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
