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

        # Photo Section
        self.photoSection = page.locator(selectors['photoSection'])
        # Property Options Panel
        self.propertyOptionsPanel = page.locator(selectors['propertyOptionsPanel'])
        self.listingStatus = self.propertyOptionsPanel.locator('[data-hc-name="listing-status"]')
        self.getPreApprovedButton = self.propertyOptionsPanel.get_by_label('Get pre-approved')
        self.contactAgentButton = self.propertyOptionsPanel.locator('[data-hc-name="contact-agent-button"]')
        self.shareButton = self.propertyOptionsPanel.get_by_label('share')
        self.saveButton = self.propertyOptionsPanel.get_by_label('Save this property to your Watchlist')
        self.mlsAttribution = self.propertyOptionsPanel.locator('.PDPRightRailCard__MLSAttribution')
        # Property Intro Section
        self.propertyIntroSection = page.locator(selectors['propertyIntroSection'])
        self.propertyFullAddress = self.propertyIntroSection.locator('h1')
        self.propertyDetails = self.propertyIntroSection.locator('h2')
        # Property Details Section
        self.propertyDetailsSection = page.locator(selectors['propertyDetailsSection'])
        self.propertyDetailsTable = self.propertyDetailsSection.locator('table')
        self.propertyDetailsCaption = self.propertyDetailsTable.locator('caption')
        self.propertyDetailsRow = self.propertyDetailsTable.locator('tr')
        self.propertyDetailsAttribution = self.propertyDetailsSection.locator('.AdditionalHomeDetails__Legal')
        # Claim Home Section
        self.claimHomeSection = page.locator(selectors['claimHomeSection'])
        self.claimHomeHeader = self.claimHomeSection.locator('.NewIcon__NewIcon')
        self.calimHomeTitle = self.claimHomeSection.locator('.HomeownerUpsellAd__Title')
        self.claimHomeDesc = self.claimHomeSection.locator('.HomeownerUpsellAd__Description')
        self.claimHomeButton = self.claimHomeSection.get_by_role('button', name='Claim home')
        # Map Section
        self.mapSection = page.locator(selectors['mapSection'])
        self.tabList = self.mapSection.get_by_role('tablist')
        self.tabListButton = self.tabList.get_by_role('tab')
        self.zoomInButton = self.mapSection.locator('[data-hc-name="zoom in"]')
        self.zoomOutButton = self.mapSection.locator('[data-hc-name="zoom out"]')
        # AVM Section
        self.avmSection = page.locator('[data-hc-name="avm-breakdown"]')

        # AVM Breakout Section
        self.avmBreakoutSection = page.locator('[data-hc-name="avm-breakout-section"]')

    # Methods
    def goto(self, slug):
        URL = self.get_url(slug)
        self.page.goto(URL)
    
    def get_property_page_details(self, data):
        details = {}
        details['full_address'] = self.construct_full_address(data)
        details['slug'] = self.construct_slug(data)
        return details
    
    def get_property_details_data(self):
        details = {}
        for row in range(self.propertyDetailsRow.count()):
            details[self.propertyDetailsRow.locator('th').nth(row).text_content()] = self.propertyDetailsRow.locator('td').nth(row).text_content()
        return details
