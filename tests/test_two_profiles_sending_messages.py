import pytest
from pages.log_in import LogInPage
from datetime import datetime


# home_page: Log in and return home_page before every test
# Pytest parameter None is to run test for the first connection on the list
# Pytest parameter 'user_2_url' is to run test for the specified connection
@pytest.mark.parametrize('connection_url',
                         [pytest.param(None), 'user_2_url'])
def test_send_message_to_connection_from_connections_panel(home_page, browser, browser_second, config, connection_url):
    user_1 = config['users'][0]
    user_2 = config['users'][1]

    if connection_url is not None:
        connection_url = user_2['url']

    local_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    message_text = f'Hi! Message sent at {local_time}.'

    # Open the second browser and login with the different user
    login_second_page = LogInPage(browser_second, user_2['username'], user_2['password'])
    home_page_second_user = login_second_page.load(). \
        accept_cookies(). \
        login()

    # Yana: Created base class Page with methods for setting of the page size/position

    # Use common methods from Page class to set the size and the position of the browsers (windows)
    home_page.\
        set_browser_width_to_half_of_the_screen().\
        set_browser_position_to_the_left()
    home_page_second_user.\
        set_browser_width_to_half_of_the_screen().\
        set_browser_position_to_the_right()

    # Click on My Network link and then on the Connections link and send the message to the first connection
    home_page.click_my_network_link(). \
        check_manage_my_network_panel_is_visible(). \
        click_connections_link().\
        send_message_to_connection(message_text, connection_url)

    result = home_page_second_user. \
        click_messaging_link(). \
        check_last_message_is_received(user_1['first_name'], user_1['last_name'], message_text)

    assert result is True, \
        f"ERROR: LinkedIn user: {user_2['username']} has not received the message."
    print(f"SUCCESS: LinkedIn user: {user_2['username']} has received the message.")

    browser.close()
    browser_second.close()
