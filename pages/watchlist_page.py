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
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
