import pytest
from pages.log_in import LogInPage


# Yana: Test Internet connection?


def test_my_network_connections_is_empty(browser, username, password):
    # Todo: Accept cookies and sign in before every test
    login_page = LogInPage(browser, username, password)
    home_page = login_page.load()\
        .accept_cookies()\
        .login()

    # Click on My Network link and then on the Connections link
    connections_page = home_page.click_my_network_link().\
        check_manage_my_network_panel_is_visible().\
        click_connections_link()

    # Verify Connections list is empty
    text = connections_page.get_empty_connections_popup_text()
    assert text == "You don’t have any connections yet."
    browser.close()
