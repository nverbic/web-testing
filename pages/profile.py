from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from pages.skills import Skills


class Profile:
    EDIT_SKILLS_LINK = (By.ID, "navigation-index-edit-skills")
    ADD_PROFILE_SECTION_BUTTON = (By.XPATH, '//div[contains(@class, "pv-top-card-v2-ctas")]/button')
    CORE_PROFILE = (By.XPATH, '//button[contains(@class, "pv-goals__section-button")]')
    CORE_PROFILE_LIST = (By.XPATH, '//div[contains(@class, "pv-goals__section-list-card")]/a')

    # Consts ?
    core_section = {
        "ADD_PROFILE_PHOTO": "Add profile photo",
        "ADD_ABOUT": "Add about",
        "ADD_EDUCATION": "Add education",
        "ADD_POSITION": "Add position",
        "ADD_CAREER_BREAK": "Add career break",
        "ADD_SKILLS": "Add skills"
    }

    def __init__(self, browser):
        self.browser = browser

    # On the user's Profile page click on the edit skills button under Skills section.
    # If the Skill section is missing, it has to be added first from the "Add to profile" section
    def edit_skills(self):
        try:
            skills = WebDriverWait(self.browser, 10).until(
                expected_conditions.element_to_be_clickable(self.EDIT_SKILLS_LINK))
            skills.click()
        except TimeoutException as e:
            print(f"Skills section is missing on the the user's profile page. Add Skills section and at least three"
                  f" skills.\n{e}")
            # Open modal dialog for adding of new sections to the profile
            self.click_add_profile_section_button()
            # Add the Skills section (under Core sections)
            self.add_core_profile_section(self.core_section["ADD_SKILLS"])
            # Open the Skills page
            skills = WebDriverWait(self.browser, 10).until(
                expected_conditions.element_to_be_clickable(self.EDIT_SKILLS_LINK))
            skills.click()

        return Skills(self.browser)

    #  From the Profile page, click on the "Add profile section" button. Opens the modal dialog with different profile
    #  sections to choose from.
    def click_add_profile_section_button(self):
        profile_sections_dialog = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.ADD_PROFILE_SECTION_BUTTON))
        profile_sections_dialog.click()
        return self

    # Add one of the core profile sections.
    def add_core_profile_section(self, profile_section):
        core_section_list = self.get_core_section_list()
        for element in core_section_list:
            if (element.text.find(profile_section)) != -1:
                element.click()
                if profile_section == self.core_section["ADD_SKILLS"]:
                    skills = Skills(self.browser)
                    skills.add_skills(3)
                elif profile_section == self.core_section["ADD_PROFILE_PHOTO"]:
                    pass
                elif profile_section == self.core_section["ADD_ABOUT"]:
                    pass
                elif profile_section == self.core_section["ADD_EDUCATION"]:
                    pass
                elif profile_section == self.core_section["ADD_POSITION"]:
                    pass
                elif profile_section == self.core_section["ADD_CAREER_BREAK"]:
                    pass
                elif profile_section == self.core_section["ADD_CAREER_BREAK"]:
                    pass
        return self

    # Get the list of profile sections under Core section (Core dropdown menu).
    # TODO: Adjust to work for all three main groups of sections, Core, Recommended and Additional
    def get_core_section_list(self):
        # Expand Core section list if needed
        core_section_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.CORE_PROFILE))
        if core_section_button.get_attribute('aria-expanded') == 'false':
            core_section_button.click()

        # Get all elements of Core list
        core_section_list = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_all_elements_located(self.CORE_PROFILE_LIST))
        return core_section_list
