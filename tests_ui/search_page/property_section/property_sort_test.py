from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_property_sort_menu(search_page: SearchPage, setup_search_page):
    """Click sort and verify sort options"""
    search_page.sortButton.click()
    expect(search_page.sortMenu.get_by_role('listbox')).to_be_visible()
    sort_options = search_page.sortMenu.get_by_role('listbox').get_by_role('option')
    expect(sort_options).to_have_count(4)
    expect(sort_options).to_have_text(['For Sale - low to high $', 'For Sale - high to low $', 'For Sale - newest to oldest', 'For Sale - oldest to newest'])
    # Click outside to close menu. NOTE: Click on sort button is blocked by menu
    search_page.body.click()
    expect(search_page.sortMenu.get_by_role('listbox')).to_be_hidden()
