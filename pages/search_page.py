import json
from playwright.sync_api import Page
from .base_page import BasePage


class SearchPage(BasePage):
    """Locators and methods for the Search Page"""
    URL = f"{BasePage.BASE_URL}search"
    TITLE = "Real estate and homes for sale | ComeHome"

    PRICE_FILTER_OPTIONS = ['$50,000', '$75,000', '$100,000', '$150,000', '$200,000', '$250,000', '$300,000',
                            '$350,000', '$400,000', '$450,000', '$500,000', '$600,000', '$700,000', '$800,000',
                            '$900,000', '$1,000,000', '$1,500,000', '$2,000,000', '$2,500,000', '$3,000,000',
                            '$3,500,000', '$4,000,000', '$4,500,000', '$5,000,000', '$6,000,000', '$7,000,000',
                            '$8,000,000', '$9,000,000', '$10,000,000']
    PROPERTY_TYPE_FILTER_OPTIONS = ['House', 'Townhouse', 'Condo', 'Co-op', 'All']
    LISTING_STATUS_FILTER_OPTIONS = ['For sale', 'Off Market', 'Pending', 'Under Contract', 'All']

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Load in common selectors from json file
        with open(BasePage.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['search_page']
        
        # Common Selectors
        self.filter_dropdown_min = '[class$=__DropdownRangeMin]'
        self.filter_dropdown_max = '[class$=__DropdownRangeMax]'

        # Search Section
        self.searchBar = page.locator(selectors['searchBar'])
        self.searchField = self.searchBar.locator('[data-hc-name=search-field]')
        self.searchInput = self.searchField.get_by_role('combobox')
        self.searchButton = self.searchField.get_by_role('button').last
        self.searchResults = self.searchField.get_by_role('listbox')
        # Price Filter
        self.priceButton = self.searchBar.locator('[data-hc-name=list-price-filter]')
        self.priceMenu = self.priceButton.get_by_role('menu')
        self.priceMinLabel = self.priceMenu.locator('[id^=left-label-]')
        self.priceMinDropdown = self.priceMenu.locator(self.filter_dropdown_min)
        self.priceMaxLabel = self.priceMenu.locator('[id^=right-label-]')
        self.priceMaxDropdown = self.priceMenu.locator(self.filter_dropdown_max)
        # Property Type Filter
        self.propertyTypeButton = self.searchBar.locator('[data-hc-name=property-type-filter]')
        self.propertyTypeMenu = self.propertyTypeButton.get_by_role('menu')
        self.propertyTypeCheckbox = self.propertyTypeMenu.locator('.Checkbox__Checkbox')
        # Beds Filter
        self.bedsButton = self.searchBar.locator('[data-hc-name=beds-filter]')
        self.bedsMenu = self.bedsButton.get_by_role('menu')
        self.bedsMenuButton = self.bedsMenu.get_by_role('button')
        self.bedsMenuLabel = self.bedsMenu.locator('.NumberAdjuster__ValueLabel')
        # More Filters
        self.moreFiltersButton = self.searchBar.locator(selectors['moreFiltersButton'])
        self.moreFiltersMenu = page.locator(selectors['moreFiltersMenu'])
        self.clearFiltersButton = self.moreFiltersMenu.locator('[data-hc-name=clear-all-filters]')
        self.filterRow = self.moreFiltersMenu.locator('[data-hc-name=filter-row]')
        self.filterRowLabel = self.filterRow.locator('[data-hc-name=row-label]')
        self.filterRowControl = self.filterRow.locator('[data-hc-name=row-control]')
        self.searchByMLSNumberLink = self.moreFiltersMenu.locator('.SearchPageFilters__MLSSearchLink')
        self.showAdvancedFiltersButton = self.moreFiltersMenu.get_by_label('Show Advanced Filters')
        # Save Search
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

    def get_filter_dropdown_options(self, dropdown_options):
        res = []
        for option in range(dropdown_options.count()):
            res.append(dropdown_options.nth(option).text_content())
        return res
    
    def get_filter_checkbox_settings(self, checkboxes, labels):
        res = {}
        for checkbox in range(checkboxes.count()):
            if checkboxes.nth(checkbox).is_checked():
                res[labels.nth(checkbox).text_content()] = True
            else:
                res[labels.nth(checkbox).text_content()] = False
        return res
