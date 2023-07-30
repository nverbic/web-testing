from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MessageDialogPopup:
    MESSAGE_DIALOG = (By.XPATH, '//*[@id="msg-overlay"]//form')
    MESSAGE_DIALOG_TEXTBOX = (By.XPATH, './/div[contains(@class,"msg-form__contenteditable")]')
    MESSAGE_DIALOG_SEND_BUTTON = (By.XPATH, './/button[@type="submit"]')

    def __init__(self, browser):
        self.browser = browser

    def send_message(self, message_text):
        # This will find the first message dialog popup window from the list
        message_dialog = WebDriverWait(self.browser, 15).\
                until(expected_conditions.visibility_of_element_located(self.MESSAGE_DIALOG))
        message_dialog.find_element(*self.MESSAGE_DIALOG_TEXTBOX).send_keys(message_text)

        # Tip: Use WebDriverWait with message_dialog instead of with self.browser (can be used on element as well!)
        WebDriverWait(message_dialog, 15).\
            until(expected_conditions.element_to_be_clickable(self.MESSAGE_DIALOG_SEND_BUTTON)).click()
