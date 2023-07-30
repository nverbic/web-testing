import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.message_dialog_popup import MessageDialogPopup


class Connections:
    EMPTY_CONNECTIONS_POPUP = (By.CLASS_NAME, "t-light")
    FIRST_CONNECTION = (By.XPATH, '//li[contains(@class, "mn-connection-card")]')
    MESSAGE_BUTTON = (By.XPATH, './/button[normalize-space()="Message"]')

    def __init__(self, browser):
        self.browser = browser

    def get_empty_connections_popup_text(self):
        connections_info = self.browser.find_element(*self.EMPTY_CONNECTIONS_POPUP)
        return connections_info.text

    def get_existing_connections_number(self):
        pass

    def get_connection_from_connections_panel(self, connection_url=None):
        if connection_url is None:
            # Get the first connection listed on the Connections panel
            connection = WebDriverWait(self.browser, 10).\
                until(expected_conditions.visibility_of_element_located(self.FIRST_CONNECTION))
            return connection
        else:
            # Todo: Add else option to search for the connection with the connection_url
            return None

    def send_message_to_connection(self, message_text, connection_url=None):
        connection = None
        if connection_url is None:
            # Get the first connection from the list
            connection = self.get_connection_from_connections_panel()

        connection.find_element(*self.MESSAGE_BUTTON).click()
        message_dialog = MessageDialogPopup(self.browser)
        message_dialog.send_message(message_text)
