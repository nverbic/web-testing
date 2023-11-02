from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from pages.skills import Skills


class Profile:
    EDIT_SKILLS_LINK = (By.ID, "navigation-index-edit-skills")

    def __init__(self, browser):
        self.browser = browser

    # On the profile page under Skills section, click on the edit skills button
    def edit_skills(self):
        try:
            skills = WebDriverWait(self.browser, 10).until(
                expected_conditions.element_to_be_clickable(self.EDIT_SKILLS_LINK))
            skills.click()
        except TimeoutException as e:
            print(f"Skills section is missing on the the user's profile page. Add at least three skills.\n{e}")
            return None
        return Skills(self.browser)
