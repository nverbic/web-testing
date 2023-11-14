import pytest
from pages.skills import Skills

MIN_NUMBER_SKILLS = 3


# Setup actions needed before test
@pytest.fixture(autouse=True, scope='function')
def preconditions(browser, home_page):
    skills_page = home_page. \
        click_home_page_welcome_panel_text(). \
        edit_skills()

    skills_num = skills_page.get_num_of_skills()

    if skills_num < MIN_NUMBER_SKILLS:
        skills_page.click_add_skills().add_skills(MIN_NUMBER_SKILLS - skills_num)

    return Skills(browser)


# home_page: Log in and return home_page before every test
# Precondition: Minimum of 3 skills added on the user's profile
def test_reorder_skills_by_dragging(browser):
    # TODO: Add source and target positions as function params?
    source_elem_pos = 2
    target_elem_pos = 0

    # Skills page is loaded in the precondition_skills_num fixture, while checking for the precondition
    skills = Skills(browser)

    result_tuple = skills. \
        open_skills_dropdown_menu(). \
        reorder_skills_by_dragging(source_elem_pos, target_elem_pos)

    # Check that the first and the third skill has swapped places
    assert result_tuple[0] is True, \
        f"ERROR:\nCould not drag and drop the {result_tuple[1]} skill from the {source_elem_pos+1}. " \
        f"position to the {target_elem_pos + 1}. position."
    print(f"SUCCESS:\nDrag and drop the skill {result_tuple[1]} from the {source_elem_pos+1}. position to the {target_elem_pos + 1}. position. \n")

    browser.close()
