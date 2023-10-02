import pytest


# home_page: Log in and return home_page before every test
def test_close_first_suggested_connection(browser, home_page):
    deleted_person_href = home_page.click_my_network_link(). \
        close_suggested_connection(). \
        find_href_in_suggested_connections_list()

    # Verify there is no suggested person with the deleted_person_href
    assert deleted_person_href is None
    browser.close()
