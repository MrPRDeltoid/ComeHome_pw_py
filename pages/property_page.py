import json
from playwright.sync_api import Page
from .base_page import BasePage


class PropertyPage(BasePage):
    """Locators and methods for the Property Page"""
    def get_url(self, slug):
        URL = f"{BasePage.BASE_URL}property-details/{slug}"
        return URL
    
    def get_title(self, address):
        TITLE = f"{address} | Property Details | ComeHome"
        return TITLE

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Load in common selectors from json file
        with open(r".\common\selectors.json", mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['property_page']

        # Top Bar Section
        self.topBar = page.locator(selectors['topBar'])

        # Photo Section
        self.photoSection = page.locator(selectors['photoSection'])

        # Property Options Panel
        self.propertyOptionsPanel = page.locator(selectors['propertyOptionsPanel'])

        # Property Intro Section
        self.propertyIntroSection = page.locator(selectors['propertyIntroSection'])

        # Property Details Section
        self.propertyDetailsSection = page.locator(selectors['propertyDetailsSection'])

        # Claim Home Section
        self.claimHomeSection = page.locator(selectors['claimHomeSection'])

        # Map Section
        self.mapSection = page.locator(selectors['mapSection'])

        # AVM Section
        self.avmSection = page.locator('[data-hc-name="avm-breakdown"]')

        # AVM Breakout Section
        self.avmBreakoutSection = page.locator('[data-hc-name="avm-breakout-section"]')

    # Methods
    def goto(self, slug):
        URL = self.get_url(slug)
        self.page.goto(URL)
