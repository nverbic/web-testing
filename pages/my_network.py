from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.connections import Connections

# Yana: Is it better to use contains instead of full link?
# Yana: The fastest way to search for an element (specify xpath as accurate as possible)?


class MyNetwork:
    MANAGE_MY_NETWORK = (By.CLASS_NAME, "mn-community-summary__section")
    SUGGESTED_PEOPLE_GROUP = (By.XPATH, "//main/ul/li[1]/ul")
    SUGGESTED_PEOPLE_LIST = (By.TAG_NAME, "li")
    SUGGESTED_PEOPLE_ITEM_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"artdeco-card__dismiss")]')
    SUGGESTED_PEOPLE_ITEM_LINK = (By.XPATH, './/a[contains(@class,"discover-entity-type-card__link")]')

    def __init__(self, browser):
        self.browser = browser
        self.deleted_suggested_connection_href = ""

    def check_manage_my_network_panel_is_visible(self):
        print("Check \"Manage my network\" panel is visible")
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(self.MANAGE_MY_NETWORK))
        return ManageMyNetworkPanel(self.browser)

    def find_href_in_suggested_people_list(self, href=None):
        if href is None:
            href = self.deleted_suggested_connection_href
        suggested_people_list = self.get_suggested_people_list()
        for li in suggested_people_list:
            if li.get_attribute('href') == href:
                return li
        return None

    def close_suggested_people_list_item(self, item_number=0):
        self.deleted_suggested_connection_href = ""
        suggested_people_list = self.get_suggested_people_list()
        print("Get person's href")
        self.deleted_suggested_connection_href = suggested_people_list[item_number].\
            find_element(*self.SUGGESTED_PEOPLE_ITEM_LINK).get_attribute('href')
        print("Close the suggested person")
        suggested_people_list[item_number].find_element(*self.SUGGESTED_PEOPLE_ITEM_CLOSE_BUTTON).click()
        return self

    def get_suggested_people_list(self):
        print("Get suggested people ul element")
        suggested_people_ul_elem = WebDriverWait(self.browser, 10). \
            until(expected_conditions.visibility_of_element_located(self.SUGGESTED_PEOPLE_GROUP))
        print("Get suggested people list of li elements")
        suggested_people_list = suggested_people_ul_elem.find_elements(*self.SUGGESTED_PEOPLE_LIST)
        return suggested_people_list


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
