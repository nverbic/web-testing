import pytest


# home_page: Log in and return home_page before every test
def test_my_network_connections_is_empty(browser, home_page):
    # Click on My Network link and then on the Connections link
    connections_page = home_page.click_my_network_link().\
        check_manage_my_network_panel_is_visible().\
        click_connections_link()

    # Verify Connections list is empty
    text = connections_page.get_empty_connections_popup_text()
    assert text == "You don’t have any connections yet.", \
        f"ERROR: Test failed: {text}"
    print(f"SUCCESS: Empty connection panel is visible on the page.")

    browser.close()
