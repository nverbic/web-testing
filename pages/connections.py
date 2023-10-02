import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.message_dialog_popup import MessageDialogPopup


class Connections:
    EMPTY_CONNECTIONS_POPUP = (By.CLASS_NAME, "t-light")
    # Yana: Is it better (quicker) to use //main//ul before //li elements when defining xpath,
    # or it makes no difference for the performance os the test?
    # Yana: /li is working also without [@class] definition. Remove it?
    # TODO: Measure performance
    CONNECTIONS_LIST = (By.XPATH, '//li[contains(@class, "mn-connection-card")]')
    CONNECTION_LINK = (By.XPATH, './/a[contains(@class,"mn-connection-card__link")]')
    MESSAGE_BUTTON = (By.XPATH, './/button[normalize-space()="Message"]')

    def __init__(self, browser):
        self.browser = browser

    def get_empty_connections_popup_text(self):
        try:
            connections_info = self.browser.find_element(*self.EMPTY_CONNECTIONS_POPUP)
            return connections_info.text
        except Exception as e:
            return f"Cannot find empty connections popup text. " \
                   f" {e}"

    def get_existing_connections_number(self):
        pass

    def get_connection_from_connections_panel(self, connection_url=None):
        if connection_url is None:
            # Get the first listed connection
            connection = WebDriverWait(self.browser, 10). \
                until(expected_conditions.visibility_of_element_located(self.CONNECTIONS_LIST))
            return connection
        else:
            connections_list = self.get_connections_list()
            # Search for the connection with the connection_url
            for connection in connections_list:
                url = connection.find_element(*self.CONNECTION_LINK).get_attribute('href')
                if connection_url in url:
                    return connection
            return None

    def send_message_to_connection(self, message_text, connection_url=None):
        connection = self.get_connection_from_connections_panel(connection_url)
        message_button = WebDriverWait(self.browser, 10).\
            until(expected_conditions.element_to_be_clickable(self.MESSAGE_BUTTON))
        message_button.click()
        message_dialog = MessageDialogPopup(self.browser)
        message_dialog.send_message(message_text)

    # Yana: When many connections, should scroll to the bottom of the page until all are loaded. Now loads just visible ones.
    def get_connections_list(self):
        print("Get list of all connections")
        # Create list
        connections_list = WebDriverWait(self.browser, 60).\
            until(expected_conditions.visibility_of_all_elements_located(self.CONNECTIONS_LIST))
        return connections_list
