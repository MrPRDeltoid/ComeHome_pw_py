from playwright.sync_api import Page
from .base_page import BasePage


class WatchlistPage(BasePage):
    """Locators and methods for the Watchlist Page"""
    URL = f"{BasePage.BASE_URL}watchlist"
    TITLE = "Saved Homes | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Header Section
        self.headerSection = self.page.locator('.WatchListHeader__WatchListHeader')
        self.savedHomesButton = self.headerSection.locator('[data-hc-name="saved-homes-button"]')
        self.savedSearchesButton = self.headerSection.locator('[data-hc-name="saved-searches-button"]')
        self.buttonTitle = self.page.locator('[data-hc-name="title"]')
        self.buttonDesc = self.page.locator('[data-hc-name="desc"]')
        self.buttonHighlight = self.page.locator('[data-hc-name="highlight"]')
        # Logged Out Section
        self.loggedOutSection = self.page.locator('[data-hc-name="logged-out-section"]')
        self.icon = self.loggedOutSection.locator('[data-hc-name="icon"]')
        self.title = self.loggedOutSection.locator('[data-hc-name="title"]')
        self.desc = self.loggedOutSection.locator('[data-hc-name="desc"]')
        self.signupButton = self.loggedOutSection.locator('[data-hc-name="signup-button]')
        self.loginButton = self.loggedOutSection.locator('[data-hc-name="login-button"]')
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
