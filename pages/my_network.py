from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.connections import Connections

# Yana: Is it better to use contains instead of full link?
# Yana: The fastest way to search for an element (specify xpath as accurate as possible)?


class MyNetwork:
    MANAGE_MY_NETWORK = (By.CLASS_NAME, "mn-community-summary__section")
    # TYPES_OF_SUGGESTED_CONNECTIONS = (By.XPATH, "//main/ul")
    # Todo: Change  hard coded first element with variable selection
    SUGGESTED_CONNECTIONS_OF_SELECTED_TYPE = (By.XPATH, "//main/ul/li[1]/ul")
    SUGGESTED_CONNECTIONS_LIST = (By.TAG_NAME, "li")
    SUGGESTED_CONNECTION_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"artdeco-card__dismiss")]')
    SUGGESTED_CONNECTION_LINK = (By.XPATH, './/a[contains(@class,"discover-entity-type-card__link")]')

    def __init__(self, browser):
        self.browser = browser
        self.deleted_suggested_connection_href = ""

    def check_manage_my_network_panel_is_visible(self):
        print("Check \"Manage my network\" panel is visible")
        WebDriverWait(self.browser, 15).until(
            expected_conditions.visibility_of_element_located(self.MANAGE_MY_NETWORK))
        return ManageMyNetworkPanel(self.browser)

    def find_href_in_suggested_connections_list(self, href=None):
        if href is None:
            href = self.deleted_suggested_connection_href
        suggested_list = self.get_suggested_connections_list()
        for connection_url in suggested_list:
            if connection_url.get_attribute('href') == href:
                return connection_url
        return None

    def close_suggested_connection(self, item_number=0):
        self.deleted_suggested_connection_href = ""
        suggested_list = self.get_suggested_connections_list()
        print("Get connection's href")
        self.deleted_suggested_connection_href = suggested_list[item_number].\
            find_element(*self.SUGGESTED_CONNECTION_LINK).get_attribute('href')
        print("Close the connection")
        suggested_list[item_number].find_element(*self.SUGGESTED_CONNECTION_CLOSE_BUTTON).click()
        return self

    # TODO: Change to work with all listed types of connections (now it works with the first displayed group
    #  of suggested connections)
    def get_suggested_connections_list(self):
        print("Get suggested connections' ul element")
        suggested_connections = WebDriverWait(self.browser, 10). \
            until(expected_conditions.visibility_of_element_located(self.SUGGESTED_CONNECTIONS_OF_SELECTED_TYPE))
        print("Get suggested connections' list of li elements")
        suggested_connections_list = suggested_connections.find_elements(*self.SUGGESTED_CONNECTIONS_LIST)
        return suggested_connections_list

    # TODO: Get list of all different types of possible connections (people, pages, follow etc.)
    # def get_suggested_connections_types(self):
    #     print("Get all suggested connections types.")
    #     suggested_types = WebDriverWait(self.browser, 10). \
    #         until(expected_conditions.visibility_of_element_located(self.TYPES_OF_SUGGESTED_CONNECTIONS))
    #     print("Get list of lists")
    #     all_suggested_types_list = suggested_types.find_elements(*self.SUGGESTED_PEOPLE_LIST)
    #     return all_suggested_types_list


class ManageMyNetworkPanel(MyNetwork):
    CONNECTIONS_LINK = (By.CLASS_NAME, "mn-community-summary__link")

    def click_connections_link(self):
        connections_elem = self.get_element_from_manage_my_network_list("Connection")
        print("Connections link click")
        connections_elem.click()
        return Connections(self.browser)

    def get_element_from_manage_my_network_list(self, element_text):
        manage_my_network_list = self.get_manage_my_network_list()
        for element in manage_my_network_list:
            # Element text can change depending on the number of connections.
            # Check if the desired text is contained in the text of the element rather than comparing strings with the equality op.
            if element.text.find(element_text) != -1:
                print(f"Get {element_text} link element from \"Manage my network\" panel.")
                return element
            else:
                return None

    def get_manage_my_network_list(self):
        print("Get list of elements under \"Manage my network\" panel.")
        manage_my_network_list = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_all_elements_located(self.CONNECTIONS_LINK))
        return manage_my_network_list
