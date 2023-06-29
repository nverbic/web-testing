from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyNetwork:
    MANAGE_MY_NETWORK = (By.CLASS_NAME, "mn-community-summary__section")

    # Yana: Is it better to use contains instead of full link?
    CONNECTIONS_LINK = (By.XPATH, '//a[@href = "/mynetwork/invite-connect/connections/"]')

    # Yana: The fastest way to search for an element (specify xpath as accurate as possible)?
    EMPTY_CONNECTIONS_POPUP = (By.CLASS_NAME, "t-light")
    #CONNECTIONS_EMPTY_DIV = (By.XPATH, "//main//*//h2[contains(text(), 'You don’t have any connections yet.')]")

    def __init__(self, browser):
        self.browser = browser

    def check_manage_my_network_panel_is_visible(self):
        print("Check \"Manage my network\" panel is visible")
        manage_network_panel = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(self.MANAGE_MY_NETWORK))
        return self

    def click_connections_link(self):
        print("Connections link click")
        connections_link = WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(self.CONNECTIONS_LINK))
        connections_link.click()
        return self

    def get_empty_connections_popup_text(self):
        connections_info = self.browser.find_element(*self.EMPTY_CONNECTIONS_POPUP)
        return connections_info.text
