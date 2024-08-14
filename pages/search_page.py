import json
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

        # Load in common selectors from json file
        with open(BasePage.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['search_page']

        # Search Section
        self.searchBar = page.locator(selectors['searchBar'])

        # Map Section
        self.mapSection = page.locator(selectors['mapSection'])

        # Property Section
        self.propertySection = page.locator(selectors['propertySection'])

    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
