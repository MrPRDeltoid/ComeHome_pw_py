from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_verify_main_sections(page: Page, home_page: HomePage, setup):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(home_page.URL)
    expect(page).to_have_title(home_page.TITLE)
    expect(home_page.mainMenu).to_be_visible()
    expect(home_page.topSection).to_be_visible()
    expect(home_page.brokerageSection.last).to_be_visible()
    expect(home_page.photoSection).to_be_visible()
    expect(home_page.trackOrBuySection).to_be_visible()
    expect(home_page.agentSection).to_be_visible()
    expect(home_page.footerSection).to_be_visible()
