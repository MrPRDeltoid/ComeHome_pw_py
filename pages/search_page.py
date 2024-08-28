import json
from playwright.sync_api import Page, Locator
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
    SQUARE_FEET_FILTER_OPTIONS = ['500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000']
    PRICE_PER_SQFT_FILTER_OPTIONS = ['$20', '$30', '$40', '$50', '$60', '$70', '$80', '$90', '$100', '$150', '$200',
                                     '$250', '$300', '$350', '$400', '$500', '$600', '$700', '$800', '$900', '$1,000']
    LOT_SIZE_FILTER_OPTIONS = ['2000 sq. ft.', '3000 sq. ft.', '4000 sq. ft.', '5000 sq. ft.', '6000 sq. ft.', '7000 sq. ft.',
                               '8000 sq. ft.', '0.25 acres', '0.50 acres', '1.00 acre', '2.00 acres', '3.00 acres', '4.00 acres',
                               '5.00 acres', '10.00 acres', '20.00 acres', '30.00 acres']
    YEAR_BUILT_FILTER_OPTIONS = ['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013',
                                 '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001',
                                 '2000', '1995', '1990', '1980', '1970', '1960', '1950', '1940', '1930', '1920', '1910', '1900']
    DAYS_ON_MARKET_FILTER_OPTIONS = ['Any', '< 1 Day', '< 3 Days', '< 7 Days', '< 14 Days', '< 30 Days', '< 90 Days']


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
        self.filter_slider_value = '.input-range__label--value'

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
        self.filterRowLabel = self.filterRow.locator('[data-hc-name=row-label], [class$=__FilterSubTitle]')
        self.filterRowControl = self.filterRow.locator('[data-hc-name=row-control]')
        self.schoolsFilterTitle = self.moreFiltersMenu.locator('legend')
        self.searchByMLSNumberLink = self.moreFiltersMenu.locator('.SearchPageFilters__MLSSearchLink')
        self.showAdvancedFiltersButton = self.moreFiltersMenu.locator('.SearchPageFilters__FiltersToggle')
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
    
    def get_filter_checkbox_settings(self, checkboxes: Locator, labels: Locator):
        res = {}
        for checkbox in range(checkboxes.count()):
            if checkboxes.nth(checkbox).is_checked():
                res[labels.nth(checkbox).text_content()] = True
            else:
                res[labels.nth(checkbox).text_content()] = False
        return res
