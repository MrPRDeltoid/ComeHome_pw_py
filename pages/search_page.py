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
        self.searchField = self.searchBar.locator('[data-hc-name=search-field]')
        self.searchInput = self.searchField.get_by_role('combobox')
        self.searchButton = self.searchField.get_by_role('button').last
        self.searchResults = self.searchField.get_by_role('listbox')
        self.priceButton = self.searchBar.locator('[data-hc-name=list-price-filter]')
        self.priceMenu = self.priceButton.get_by_role('menu')
        self.propertyTypeButton = self.searchBar.locator('[data-hc-name=property-type-filter]')
        self.propertyTypeMenu = self.propertyTypeButton.get_by_role('menu')
        self.bedsButton = self.searchBar.locator('[data-hc-name=beds-filter]')
        self.bedsMenu = self.bedsButton.get_by_role('menu')
        self.moreFiltersButton = self.searchBar.locator('[data-hc-name=filters-filter]')
        self.moreFiltersMenu = page.locator('[data-hc-name=tooltip-content]')
        self.saveSearchButton = self.searchBar.locator('[data-hc-name=save-filter-button]')
        # Map Section
        self.mapSection = page.locator(selectors['mapSection'])

        # Property Section
        self.propertySection = page.locator(selectors['propertySection'])

    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
    
    def search_for_property(self, property):
        self.searchInput.fill(property)
        self.searchButton.click()
