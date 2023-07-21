from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from pages.home import HomePage


class LogInPage:
    URL = 'https://www.linkedin.com/home/'
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//*[@class="artdeco-global-alert-action__wrapper"]//button[@action-type=\'ACCEPT\']')
    USERNAME_TEXTBOX_OPTION_1 = (By.ID, "session_key")
    PASSWORD_TEXTBOX_OPTION_1 = (By.ID, "session_password")
    # TODO: If OPTION_1 ids above are not available, check with the OPTION_2 ids below
    # USERNAME_TEXTBOX_OPTION_2 = (By.ID, "username")
    # PASSWORD_TEXTBOX_OPTION_2 = (By.ID, "password")

    SIGNIN_BUTTON = (By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
    # If join-in dialog is displayed, check for the sign-in button and retry to log in
    LINK_TO_SIGNIN_PAGE = (By.CLASS_NAME, "authwall-join-form__form-toggle--bottom")

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
            accept_button = WebDriverWait(self.browser, 20).until(expected_conditions.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON))
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"An exception occurred: {str(e)}")
            self.browser.refresh()
            print("Refresh page")
            accept_button = WebDriverWait(self.browser, 20).until(expected_conditions.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON))
            print("Accept cookies after refresh")
        # print(accept_button.get_attribute('action-type'))
        accept_button.click()
        return self

    def login(self):
        print("Check for login input fields")
        try:
            username = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.USERNAME_TEXTBOX_OPTION_1))
            password = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.PASSWORD_TEXTBOX_OPTION_1))
        except TimeoutException:
            link_to_sign_in_page = self.browser.find_element(*self.LINK_TO_SIGNIN_PAGE)
            link_to_sign_in_page.click()
            username = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.USERNAME_TEXTBOX_OPTION_1))
            password = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.PASSWORD_TEXTBOX_OPTION_1))
        print("Enter credentials")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        print("Sign in")
        sign_in_button = self.browser.find_element(*self.SIGNIN_BUTTON)
        sign_in_button.click()
        return HomePage(self.browser)


