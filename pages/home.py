from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage:
    WELCOME_PANEL = (By.XPATH, '//div[contains(@class, "feed-identity-module__actor-meta")]')

    def __init__(self, browser):
        self.browser = browser

    def get_home_page_welcome_panel_text(self):
        personal_info = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located(self.WELCOME_PANEL))
        #print(personal_info.text)
        return len(personal_info.text)
