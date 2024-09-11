import json
from playwright.sync_api import Page
from .base_page import BasePage


class HomeownerPage(BasePage):
    """Locators and methods for the Homeowner Page"""
    URL = f"{BasePage.BASE_URL}homeowner"
    TITLE = "My Home | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Load in common selectors from json file
        with open(BasePage.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['homeowner_page']

        # Main Section(shown when no address is selected)
        self.mainSection = self.page.locator(selectors['mainSection'])

        # AVM Section
        self.avmSection = self.page.locator(selectors['avmSection'])
        self.avmSectionAddress = self.avmSection.locator('[data-hc-name=avm-address]').locator('h1')
        self.avmSectionDetails = self.avmSection.locator('[data-hc-name=avm-property-details]')

        # Property Cards Section
        self.cardsSection = self.page.locator(selectors['cardsSection'])

    # Methods
    def getUrlProperty(self, slug):
        """Given the slug, get the URL when a property is loaded in the Homowner page"""
        property_url = f"{self.URL}/{slug}"
        return property_url
    
    def getTitleProperty(self, address):
        """Given the full address, get the Title when a property is loaded in the Homowner page"""
        property_title = f"{address} | {self.TITLE}"
        return property_title
    
    def goto(self):
        self.page.goto(self.URL)
