from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5000"  # Or your app's URL

def test_homepage_baseline(page: Page):
    """Step 3: Capture baseline screenshot"""
    page.goto(BASE_URL)
    # Baseline screenshot — first run creates reference
    expect(page).to_have_screenshot("homepage-baseline", threshold=0.1)

def test_ui_change_detection(page: Page):
    """Step 4-5: After making a change, run to see diff"""
    page.goto(BASE_URL)
    expect(page).to_have_screenshot("homepage-baseline", threshold=0.1)