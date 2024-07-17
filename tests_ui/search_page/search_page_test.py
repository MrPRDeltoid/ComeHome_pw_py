from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_verify_main_sections(page: Page, search_page: SearchPage, setup_search_page):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(search_page.URL)
    expect(page).to_have_title(search_page.TITLE)
    expect(search_page.mainMenu).to_be_visible()
    expect(search_page.searchBar).to_be_visible()
    expect(search_page.mapSection).to_be_visible()
    expect(search_page.propertySection).to_be_visible()
    search_page.footerSection.scroll_into_view_if_needed()
    expect(search_page.footerSection).to_be_visible()
