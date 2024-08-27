from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_beds_filter_menu(search_page: SearchPage, setup_search_page):
    """Click the Beds filter button and verify menu contents"""
    expect(search_page.bedsButton).to_have_text('Beds: Any')
    search_page.bedsButton.click()
    expect(search_page.bedsMenu).to_be_visible()
    expect(search_page.bedsMenuButton.first).to_have_text('-')
    expect(search_page.bedsMenuButton.first).to_be_disabled()
    expect(search_page.bedsMenuLabel).to_have_text('0+')
    expect(search_page.bedsMenuButton.last).to_have_text('+')
    expect(search_page.bedsMenuButton.last).to_be_enabled()
