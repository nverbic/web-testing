import pytest


# home_page: Log in and return home_page before every test
def test_sign_in(browser, home_page):
    # Verify login is success by locating identity panel on the page
    assert home_page.get_home_page_welcome_panel_text() > 0
    browser.close()
