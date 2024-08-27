from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_property_type_filter_menu(search_page: SearchPage, setup_search_page):
    """Click the Property Type filter button and verify menu options"""
    expect(search_page.propertyTypeButton).to_have_text('Property Type: All')
    search_page.propertyTypeButton.click()
    expect(search_page.propertyTypeMenu).to_be_visible()
    checkboxes = search_page.propertyTypeMenu.get_by_role('checkbox')
    labels = search_page.propertyTypeCheckbox.locator('label')
    # Verify correct labels and default check state for each checkbox
    assert search_page.get_filter_checkbox_settings(checkboxes, labels) == {'House': False,
                                                                            'Townhouse': False,
                                                                            'Condo': False,
                                                                            'Co-op': False,
                                                                            'All': True}
