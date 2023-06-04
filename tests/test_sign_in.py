import pytest

from pages.log_in import LogInPage
from pages.home import HomePage


def test_sign_in(browser, username, password):
    # Accept cookies and sign in
    login_page = LogInPage(browser, username, password)
    login_page.load()
    login_page.accept_cookies()
    login_page.login()

    # Verify login is success by locating identity panel on the page
    home_page = HomePage(browser)
    assert home_page.feed_identity_module_text() > 0
    browser.close()