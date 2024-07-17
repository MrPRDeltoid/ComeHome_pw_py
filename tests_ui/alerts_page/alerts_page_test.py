from playwright.sync_api import Page, expect
from pages.alerts_page import AlertsPage


def test_verify_main_sections(page: Page, alerts_page: AlertsPage, setup_alerts_page):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(alerts_page.URL)
    expect(page).to_have_title(alerts_page.TITLE)
    expect(alerts_page.mainMenu).to_be_visible()
    expect(alerts_page.headerSection).to_be_visible()
    expect(alerts_page.loggedOutSection).to_be_visible()
    expect(alerts_page.footerSection).to_be_visible()
