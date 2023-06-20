from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class LogInPage:
    URL = 'https://www.linkedin.com/home/'
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//*[@class="artdeco-global-alert-action__wrapper"]//button[@action-type=\'ACCEPT\']')
    USERNAME_TEXTBOX = ((By.ID, "session_key" or "username"))
    PASSWORD_TEXTBOX = (By.ID, ("session_password" or "password"))
    SIGNIN_BUTTON = (By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")

    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    def load(self):
        self.browser.maximize_window()
        print("\nLoad URL")
        self.browser.get(self.URL)
        return self

    def accept_cookies(self):
        print("Accept cookies")
        try:
            accept_button = WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON))
        except TimeoutException:
            print("Timeout loading page")
            self.browser.refresh()
            print("Refresh page")
            accept_button = WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON))
            print("Accept cookies after refresh")
        # print(accept_button.get_attribute('action-type'))
        accept_button.click()
        return self

    def login(self):
        print("Check for login input fields")
        username = self.browser.find_element(*self.USERNAME_TEXTBOX)
        password = self.browser.find_element(*self.PASSWORD_TEXTBOX)
        print("Enter credentials")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        print("Sign in")
        sign_in_button = self.browser.find_element(*self.SIGNIN_BUTTON)
        sign_in_button.click()
        return self

