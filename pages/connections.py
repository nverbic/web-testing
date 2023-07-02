from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Connections:
    EMPTY_CONNECTIONS_POPUP = (By.CLASS_NAME, "t-light")

    def __init__(self, browser):
        self.browser = browser

    def get_empty_connections_popup_text(self):
        connections_info = self.browser.find_element(*self.EMPTY_CONNECTIONS_POPUP)
        return connections_info.text

    def get_existing_connections_number(self):
        pass


