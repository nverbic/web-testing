from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.connections import Connections

# Yana: Is it better to use contains instead of full link?
# Yana: The fastest way to search for an element (specify xpath as accurate as possible)?


class MyNetwork:
    MANAGE_MY_NETWORK = (By.CLASS_NAME, "mn-community-summary__section")

    def __init__(self, browser):
        self.browser = browser

    def check_manage_my_network_panel_is_visible(self):
        print("Check \"Manage my network\" panel is visible")
        manage_network_panel = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(self.MANAGE_MY_NETWORK))
        return ManageMyNetworkPanel(self.browser)


class ManageMyNetworkPanel(MyNetwork):
    CONNECTIONS_LINK = (By.CLASS_NAME, "mn-community-summary__link")

    def click_connections_link(self):
        connections_elem = self.get_element_from_manage_my_network_list("Connections")
        print("Connections link click")
        connections_elem.click()
        return Connections(self.browser)

    def get_element_from_manage_my_network_list(self, element_text):
        manage_my_network_list = self.get_manage_my_network_list()
        for element in manage_my_network_list:
            if element.text == element_text:
                print(f"Get {element_text} link element from \"Manage my network\" panel.")
                return element
            else:
                return None

    def get_manage_my_network_list(self):
        print("Get list of elements under \"Manage my network\" panel.")
        manage_my_network_list = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_all_elements_located(self.CONNECTIONS_LINK))
        return manage_my_network_list
