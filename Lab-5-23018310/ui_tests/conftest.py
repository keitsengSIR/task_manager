"""Browser fixture.

No HEALENIUM_URL set  -> local Chrome (used for baseline and the 'without Healenium' run)
HEALENIUM_URL set     -> remote browser through the Healenium proxy (e.g. http://localhost:8085)
BASE_URL              -> address of the web app as seen BY THE BROWSER
"""
import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "http://localhost:5000")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
    healenium = os.environ.get("HEALENIUM_URL")
    if healenium:
        drv = webdriver.Remote(command_executor=healenium, options=options)
    else:
        drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(0)   # we use explicit waits only, so failures are quick and clear
    yield drv
    drv.quit()
