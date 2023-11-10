from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class Skills:
    SKILLS_GROUP = (By.XPATH, "//main//ul[@class='pvs-list ']")
    SKILLS_LIST = (By.XPATH, "./li")
    SKILLS_DROPDOWN_MENU = (By.ID, "overflow-more")
    REORDER_SKILLS_LINK = (By.XPATH, '//div[contains(@class, "artdeco-dropdown__content-inner")]//a')
    REORDER_SKILLS_DIALOG_LIST = (By.XPATH, '//div[contains(@class, "artdeco-modal__content")]//ul//li')
    MOVE_SKILL_BUTTON = (By.TAG_NAME, 'button')
    ADD_SKILLS_LINK = (By.ID, "navigation-add-edit-deeplink-add-skills")
    SKILL_FROM_SUGGESTED_LIST_BUTTON = (By.XPATH, "//div[@id='artdeco-modal-outlet']//fieldset/button")
    SAVE_SKILL_BUTTON = (By.XPATH, "//div[@id='artdeco-modal-outlet']//button[@data-view-name='profile-form-save']")
    ADD_MORE_SKILLS_BUTTON = (By.XPATH,
                              "//div[@id='artdeco-modal-outlet']//div[contains(@class, 'artdeco-modal__actionbar')]/button")
    CLOSE_ADD_SKILLS = (By.XPATH, "//button[@aria-label='Dismiss']")

    def __init__(self, browser):
        self.browser = browser
        self.skills = []

    # On the Skills page get a list of skills and return its length
    def get_num_of_skills(self):
        # Create list
        skills = WebDriverWait(self.browser, 10).\
             until(expected_conditions.visibility_of_element_located(self.SKILLS_GROUP))
        skills_list = skills.find_elements(*self.SKILLS_LIST)
        skills_num = len(skills_list)
        return skills_num

    # On the Skills page click add (plus sign) button to add skills
    def click_add_skills(self):
        add = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.ADD_SKILLS_LINK))
        add.click()
        return self

    # Add new skill from the box of the suggested skills by selecting the first skill from the list.
    # skills_num = the number of skills to be added
    def add_skills(self, skills_num):
        for i in range(skills_num):
            skill = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.SKILL_FROM_SUGGESTED_LIST_BUTTON))
            skill.click()
            save_button = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.SAVE_SKILL_BUTTON))
            save_button.click()
            add_more_skills_button = WebDriverWait(self.browser, 20).until(
                expected_conditions.element_to_be_clickable(self.ADD_MORE_SKILLS_BUTTON))
            add_more_skills_button.click()

        # Important: wait for the dialog to reload after the last skill is added
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(self.SKILL_FROM_SUGGESTED_LIST_BUTTON))

        close_button = WebDriverWait(self.browser, 20).until(
            expected_conditions.element_to_be_clickable(self.CLOSE_ADD_SKILLS))
        close_button.click()

    # On the Skills' page click on the button (three dots) to open the dropdown menu.
    def open_skills_dropdown_menu(self):
        drop_down_menu = WebDriverWait(self.browser, 20).until(
            expected_conditions.element_to_be_clickable(self.SKILLS_DROPDOWN_MENU))
        drop_down_menu.click()
        return self

    # From Skills' dropdown menu, click reorder button to open the modal dialog for reordering of the skills
    def click_reorder_skills(self):
        reorder = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.REORDER_SKILLS_LINK))
        reorder.click()
        return self

    def reorder_skills_by_dragging(self, source_elem_position, target_elem_position):
        self.click_reorder_skills()
        self.get_list_of_skills_from_reorder_dialog()
        source_element = self.skills[source_elem_position]
        source_dragging_button = self.skills[source_elem_position].find_element(*self.MOVE_SKILL_BUTTON)
        target_element = self.skills[target_elem_position]
        print(
            f"Drag and drop the {source_elem_position + 1}. skill from the list, to the {target_elem_position + 1}. "
            f"position.")
        action = ActionChains(self.browser)
        action.click_and_hold(source_dragging_button).\
            move_to_element(target_element).\
            move_by_offset(0, -10).\
            release().\
            pause(1).\
            perform()

        # Load the list again and check that the source element is moved to the target element position
        self.get_list_of_skills_from_reorder_dialog()
        if self.skills[target_elem_position] == source_element:
            return True, source_element.text
        else:
            return False, source_element.text

    # Get list of skills from the modal dialog for reordering of the skills
    def get_list_of_skills_from_reorder_dialog(self):
        print("Get list of skills")
        # Create list
        self.skills = WebDriverWait(self.browser, 60).\
            until(expected_conditions.visibility_of_all_elements_located(self.REORDER_SKILLS_DIALOG_LIST))

