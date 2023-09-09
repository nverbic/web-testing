from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Messaging:
    MESSAGING_PANEL = (By.XPATH, '//ul[contains(@class,"msg-conversations-container__conversations-list")]')
    MESSAGING_LIST = (By.TAG_NAME, "li")
    NEW_CONVERSATION_THREAD_LINK = (By.XPATH, '//li//a[contains(@class, "msg-conversation-listitem__link")]')
    NEW_CONVERSATION_THREAD_LAST_MESSAGE = (By.XPATH, "//li//p")

    def __init__(self, browser):
        self.browser = browser

    # Check for the specific message in the list of all messages
    # TODO: Check when there are many messages and need scrolling
    def check_message_is_received(self, first_name, last_name, message_text):
        message_data = [first_name, last_name, message_text]
        messages_list = self.get_messages_list()
        for message in messages_list:
            if all([data in message.text for data in message_data]):
                print(f"Message received: \n{message.text} ")
                return True
        return False

    def check_last_message_is_received(self, first_name, last_name, message_text):
        message_contact = [first_name, last_name]
        # In the Messaging list of the conversations, the last conversation, with the newly received message,
        # is displayed at the top of the list.
        last_received_message = WebDriverWait(self.browser, 10). \
            until(expected_conditions.element_to_be_clickable(self.NEW_CONVERSATION_THREAD_LINK))
        # If the contact details are correct, check if the new message in the conversation thread is the same as in the
        # parameter "message_text".
        # NOTE: The conversation thread is automatically opened and focused (no need (and not possible) to click
        # on the contact in the Messaging list)
        if all([data in last_received_message.text for data in message_contact]):
            print(f"Message received: \n{last_received_message.text} ")
            try:
                found_last_message_in_the_conversation = WebDriverWait(self.browser, 10). \
                    until(expected_conditions.text_to_be_present_in_element(self.NEW_CONVERSATION_THREAD_LAST_MESSAGE, message_text))
                return found_last_message_in_the_conversation
            except Exception as e:
                print(e)
                # TODO: Pass more specific error message to the test, depending on where the error was found ...
                return False
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
