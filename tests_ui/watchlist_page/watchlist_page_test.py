from playwright.sync_api import Page, expect
from pages.watchlist_page import WatchlistPage


def test_verify_main_sections(page: Page, watchlist_page: WatchlistPage, setup_watchlist_page):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(watchlist_page.URL)
    expect(page).to_have_title(watchlist_page.TITLE)
    expect(watchlist_page.mainMenu).to_be_visible()
    expect(watchlist_page.headerSection).to_be_visible()
    expect(watchlist_page.loggedOutSection).to_be_visible()
    expect(watchlist_page.footerSection).to_be_visible()
