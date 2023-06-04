from selenium.webdriver.common.by import By


class HomePage:
    FEED_IDENTITY_MODULE = (By.XPATH, '//*[@class="feed-identity-module artdeco-card overflow-hidden mb2"]')

    def __init__(self, browser):
        self.browser = browser

    def feed_identity_module_text(self):
        # personal_info = ""
        personal_info = self.browser.find_element(*self.FEED_IDENTITY_MODULE)
        return len(personal_info.text)
