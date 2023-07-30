from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Messaging:
    MESSAGING_PANEL = (By.XPATH, '//ul[contains(@class,"msg-conversations-container__conversations-list")]')
    MESSAGING_LIST = (By.TAG_NAME, "li")

    def __init__(self, browser):
        self.browser = browser

    # Check for the specific message in the list of all messages
    def check_message_is_received(self, firs_name, last_name, message_text):
        message_data = [firs_name, last_name, message_text]

        messages_list = self.get_messages_list()
        for message in messages_list:
            if all([data in message.text for data in message_data]):
                print(f"Message received: \n{message.text} ")
                return True
        return False

    # Get a list of all messages
    def get_messages_list(self):
        print("Get list of all messages")
        # Get the "ul" element of Messaging panel list
        messaging_panel = WebDriverWait(self.browser, 10). \
            until(expected_conditions.visibility_of_element_located(self.MESSAGING_PANEL))
        # Create list
        messages_list = messaging_panel.find_elements(*self.MESSAGING_LIST)
        return messages_list


