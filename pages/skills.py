from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class Skills:
    SKILLS_GROUP = (By.XPATH, "//main//ul[@class='pvs-list ']")
    SKILLS_LIST = (By.TAG_NAME, "li")
    SKILLS_DROPDOWN_MENU = (By.ID, "overflow-more")
    OPEN_REORDER_SKILLS_DIALOG_LINK = (By.XPATH, '//div[contains(@class, "artdeco-dropdown__content-inner")]//a')
    REORDER_SKILLS_DIALOG_LIST = (By.XPATH, '//div[contains(@class, "artdeco-modal__content")]//ul//li')
    MOVE_SKILL_BUTTON = (By.TAG_NAME, 'button')

    def __init__(self, browser):
        self.browser = browser
        self.skills = []

    # On the Skill's page get a list of skills and return its length
    def get_num_of_skills(self):
        # Create list
        skills = WebDriverWait(self.browser, 10).\
            until(expected_conditions.visibility_of_element_located(self.SKILLS_GROUP))
        skills_list = skills.find_elements(*self.SKILLS_LIST)
        skills_num = len(skills_list)
        return skills_num

    # On the Skills' page click on the button (three dots) to open the dropdown menu.
    def open_skills_dropdown_menu(self):
        drop_down_menu = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.SKILLS_DROPDOWN_MENU))
        drop_down_menu.click()
        return self

    # From Skills' dropdown menu, click reorder button to open the modal dialog for reordering of the skills
    def click_skills_reorder(self):
        reorder = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(self.OPEN_REORDER_SKILLS_DIALOG_LINK))
        reorder.click()
        return self

    def reorder_skills_by_dragging(self, source_elem_position, target_elem_position):
        self.click_skills_reorder()
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
            pause(2).\
            perform()

        # Load the list again and check that the source element is moved to the target element position
        self.get_list_of_skills_from_reorder_dialog()
        if self.skills[target_elem_position] == source_element:
            return True, source_element.text
        else:
            return False, source_element.text

    # Get list of skills from the modal dialog for reordering of the skills
    # TODO: Get list from the main skill's page
    def get_list_of_skills_from_reorder_dialog(self):
        print("Get list of skills")
        # Create list
        self.skills = WebDriverWait(self.browser, 60).\
            until(expected_conditions.visibility_of_all_elements_located(self.REORDER_SKILLS_DIALOG_LIST))

