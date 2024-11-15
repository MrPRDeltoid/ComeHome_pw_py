from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_click_button_logged_out(search_page: SearchPage, setup_search_page):
    """Click the Save Search button when not logged in to verify signin dialog appears"""
    expect(search_page.saveSearchButton).to_be_visible()
    search_page.saveSearchButton.click()
    expect(search_page.joinLoginDialog).to_be_visible()
    search_page.closeDialog()
    expect(search_page.joinLoginDialog).not_to_be_visible()
