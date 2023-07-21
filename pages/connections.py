import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Connections:
    EMPTY_CONNECTIONS_POPUP = (By.CLASS_NAME, "t-light")
    FIRST_CONNECTION = (By.XPATH, '//li[contains(@class, "mn-connection-card")]')
    MESSAGE_DIV = (By.XPATH, './/div[contains(@class, "mn-connection-card__action-container")]')
    MESSAGE_BUTTON = (By.XPATH, './/button[normalize-space()="Message"]')
    MESSAGE_DIALOG = (By.XPATH, '//*[@id="msg-overlay"]//form')
    MESSAGE_DIALOG_TEXTBOX = (By.XPATH, './/div[contains(@class,"msg-form__contenteditable")]')
    MESSAGE_DIALOG_SEND_BUTTON = (By.XPATH, './/button[@type="submit"]')

    def __init__(self, browser):
        self.browser = browser

    def get_empty_connections_popup_text(self):
        connections_info = self.browser.find_element(*self.EMPTY_CONNECTIONS_POPUP)
        return connections_info.text

    def get_existing_connections_number(self):
        pass

    def get_first_connection(self):
        first_connection = WebDriverWait(self.browser, 10).\
            until(expected_conditions.visibility_of_element_located(self.FIRST_CONNECTION))
        print(first_connection)
        action_panel = self.browser.find_element(*self.MESSAGE_DIV)
        print(action_panel)
        message_button = self.browser.find_element(*self.MESSAGE_BUTTON)
        print(message_button)
        message_button.click()
        message_dialog = WebDriverWait(self.browser, 15).until(expected_conditions.visibility_of_element_located(self.MESSAGE_DIALOG))
        print(message_dialog)
        message_dialog_textbox = message_dialog.find_element(*self.MESSAGE_DIALOG_TEXTBOX)
        message_dialog_textbox.send_keys("Hi there!")
        time.sleep(5)
        message_dialog_send_button = message_dialog.find_element(*self.MESSAGE_DIALOG_SEND_BUTTON)
        print(message_dialog_send_button)
        message_dialog_send_button.click()
        time.sleep(5)
