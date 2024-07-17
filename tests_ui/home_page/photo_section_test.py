from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_correct_text_and_elements(home_page: HomePage, setup):
    """Verify Agent section has correct text and elements"""
    expect(home_page.photoColumn).to_have_count(4)
    expect(home_page.photo).to_have_count(10)
