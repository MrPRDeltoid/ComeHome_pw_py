from playwright.sync_api import Page, expect
from pages.homeowner_page import HomeownerPage


def test_verify_main_sections(page: Page, homeowner_page: HomeownerPage, setup_homeowner_page):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(homeowner_page.URL)
    expect(page).to_have_title(homeowner_page.TITLE)
    expect(homeowner_page.mainMenu).to_be_visible()
    expect(homeowner_page.mainSection).to_be_visible()
    expect(homeowner_page.footerSection).to_be_visible()
