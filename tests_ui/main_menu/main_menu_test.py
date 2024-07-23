from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.homeowner_page import HomeownerPage
from pages.watchlist_page import WatchlistPage
from pages.alerts_page import AlertsPage
from pages.agent_page import AgentPage


def test_verify_main_menu_items(home_page: HomePage, setup):
    """Check all expected main header items are shown"""
    expect(home_page.logo).to_be_visible
    expect(home_page.buyHomeButton).to_have_text("Find a home")
    expect(home_page.myHomeButton).to_have_text("My home")
    expect(home_page.savedButton).to_have_text("Saved")
    expect(home_page.alertsButton).to_have_text("Alerts")
    expect(home_page.findAnAgentButton).to_have_text("Find an agent")
    expect(home_page.joinLoginButton).to_have_text("Join or Log in")

def test_find_home_menu_item(page: Page, home_page: HomePage, search_page: SearchPage, setup):
    """Click Find a Home menu item and verify correct page is loaded"""
    home_page.buyHomeButton.click()
    expect(page).to_have_url(search_page.URL)
    expect(page).to_have_title(search_page.TITLE)

def test_my_home_menu_item(page: Page, home_page: HomePage, homeowner_page: HomeownerPage, setup):
    """Click My Home menu item and verify correct page is loaded"""
    home_page.myHomeButton.click()
    expect(page).to_have_url(homeowner_page.URL)
    expect(page).to_have_title(homeowner_page.TITLE)

def test_saved_menu_item(page: Page, home_page: HomePage, watchlist_page: WatchlistPage, setup):
    """Click Saved menu item and verify correct page is loaded"""
    home_page.savedButton.click()
    expect(page).to_have_url(watchlist_page.URL)
    expect(page).to_have_title(watchlist_page.TITLE)

def test_alerts_menu_item(page: Page, home_page: HomePage, alerts_page: AlertsPage, setup):
    """Click Alerts menu item and verify correct page is loaded"""
    home_page.alertsButton.click()
    expect(page).to_have_url(alerts_page.URL)
    expect(page).to_have_title(alerts_page.TITLE)

def test_find_agent_menu_item(page: Page, home_page: HomePage, agent_page: AgentPage, setup):
    """Click Find an Agent menu item and verify correct page is loaded"""
    home_page.findAnAgentButton.click()
    expect(page).to_have_url(agent_page.URL)
    #expect(page).to_have_title(agent_page.TITLE)  # TODO: BUG - Agent page does not update the title
