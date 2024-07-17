from playwright.sync_api import Page
from .base_page import BasePage


class SearchPage(BasePage):
    """Locators and methods for the Search Page"""
    URL = f"{BasePage.BASE_URL}search"
    TITLE = "Real estate and homes for sale | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
