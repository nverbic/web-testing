from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.my_network import MyNetwork
from pages.messaging import Messaging
from pages.profile import Profile
from pages.page import Page


class HomePage(Page):
    def __init__(self, browser, width=0, height=0):
        super().__init__(browser, width, height)

    WELCOME_PANEL = (By.XPATH, '//div[contains(@class, "feed-identity-module__actor-meta")]')

    # TODO: Check if href link corresponds to the user's link in config file
    WELCOME_PANEL_MY_PROFILE_LINK = (By.XPATH, '//div[contains(@class, "feed-identity-module__actor-meta")]/a')
    MY_NETWORK_LINK = (By.XPATH, '//a[@href = "https://www.linkedin.com/mynetwork/?"]')
    MESSAGING_LINK = (By.XPATH, '//a[@href = "https://www.linkedin.com/messaging/?"]')

    def get_home_page_welcome_panel_text(self):
        personal_info = WebDriverWait(self.browser, 15).until(expected_conditions.presence_of_element_located(self.WELCOME_PANEL))
        return len(personal_info.text)

    def click_home_page_welcome_panel_text(self):
        personal_info = WebDriverWait(self.browser, 15).\
            until(expected_conditions.element_to_be_clickable(self.WELCOME_PANEL_MY_PROFILE_LINK))
        personal_info.click()
        return Profile(self.browser)

    def click_my_network_link(self):
        print("Click \"My Network\" link")
        my_network_link = WebDriverWait(self.browser, 15).until(expected_conditions.element_to_be_clickable(self.MY_NETWORK_LINK))
        my_network_link.click()
        return MyNetwork(self.browser)

    def click_messaging_link(self):
        print("Click \"Messaging\" link")
        messaging_link = WebDriverWait(self.browser, 15).until(expected_conditions.element_to_be_clickable(self.MESSAGING_LINK))
        messaging_link.click()
        return Messaging(self.browser)
