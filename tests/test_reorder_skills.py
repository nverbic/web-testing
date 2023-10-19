import pytest


# home_page: Log in and return home_page before every test
def test_reorder_skills_by_dragging(browser, home_page):
    # TODO: Add source and target positions as function params?
    source_elem_pos = 2
    target_elem_pos = 0
    result_tuple = home_page. \
        click_home_page_welcome_panel_text(). \
        edit_skills(). \
        open_skills_dropdown_menu(). \
        reorder_skills_by_dragging(source_elem_pos, target_elem_pos)

    # Check that the first and the third skill has swapped places
    assert result_tuple[0] is True, \
        f"ERROR:\nCould not drag and drop the {result_tuple[1]} skill from the {source_elem_pos+1}. " \
        f"position to the {target_elem_pos + 1}. position."
    print(f"SUCCESS:\nDrag and drop the skill {result_tuple[1]} from the {source_elem_pos+1}. position to the {target_elem_pos + 1}. position. \n")

    browser.close()
