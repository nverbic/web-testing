import pytest
from pages.log_in import LogInPage
from datetime import datetime


# home_page: Log in and return home_page before every test
# Pytest parameter None is to run test for the first connection on the list
# Pytest parameter 'user_2_url' is to run test for the specified connection
@pytest.mark.parametrize('connection_url',
                         [pytest.param(None), 'user_2_url'])
def test_send_message_to_connection_from_connections_panel(home_page, browser, first_name, last_name, browser_second,
                                                           username_user_2, password_user_2, connection_url, request):
    if connection_url is None:
        connection_url = None
    else:
        connection_url = request.getfixturevalue(connection_url)

    local_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    message_text = f'Hi! Message sent at {local_time}.'

    # Click on My Network link and then on the Connections link and send the message to the first connection
    home_page.click_my_network_link(). \
        check_manage_my_network_panel_is_visible(). \
        click_connections_link().\
        send_message_to_connection(message_text, connection_url)
    browser.close()

    login_second_page = LogInPage(browser_second, username_user_2, password_user_2)
    home_page_second_user = login_second_page.load(). \
        accept_cookies(). \
        login()
    result = home_page_second_user.\
        click_messaging_link().\
        check_message_is_received(first_name, last_name, message_text)

    assert result is True
    browser_second.close()
