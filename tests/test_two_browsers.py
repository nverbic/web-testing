import pytest
from pages.connections import Connections
from pages.log_in import LogInPage
import time


# home_page: Log in and return home_page before every test
# TODO: Add params: username_second, password_second, browser_second)
def test_send_message_to_connection(home_page, browser):
    # Click on My Network link and then on the Connections link
    connections_page = home_page.click_my_network_link(). \
        check_manage_my_network_panel_is_visible(). \
        click_connections_link()

    connections_page.get_first_connection()
    time.sleep(5)
    browser.close()

    # TODO: Implement checking of the message from the second browser
    # login_second_page = LogInPage(browser_second, username_second, password_second)
    # home_page_second_user = login_second_page.load(). \
    #     accept_cookies(). \
    #     login()
    # browser_second.close()


