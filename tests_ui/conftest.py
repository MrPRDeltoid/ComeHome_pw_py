import pytest
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.homeowner_page import HomeownerPage
from pages.watchlist_page import WatchlistPage
from pages.alerts_page import AlertsPage
from pages.agent_page import AgentPage
from pages.property_page import PropertyPage


@pytest.fixture()
def setup(page: Page, home_page: HomePage):
    home_page.goto()
    page.set_viewport_size({"width": 1920, "height": 1080})

@pytest.fixture()
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture()
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture()
def search_page(page: Page):
    return SearchPage(page)

@pytest.fixture()
def homeowner_page(page: Page):
    return HomeownerPage(page)

@pytest.fixture()
def watchlist_page(page: Page):
    return WatchlistPage(page)

@pytest.fixture()
def alerts_page(page: Page):
    return AlertsPage(page)

@pytest.fixture()
def agent_page(page: Page):
    return AgentPage(page)

@pytest.fixture()
def property_page(page: Page):
    return PropertyPage(page)
