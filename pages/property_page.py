import json
from playwright.sync_api import Page
from .base_page import BasePage


class PropertyPage(BasePage):
    """Locators and methods for the Property Page"""
    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Load in common selectors from json file
        with open(BasePage.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['property_page']

        # Photo Section
        self.photoSection = page.locator(selectors['photoSection'])
        # Property Options Panel
        self.propertyOptionsPanel = page.locator(selectors['propertyOptionsPanel'])
        self.listingStatus = self.propertyOptionsPanel.locator('[data-hc-name=listing-status]')
        self.listingStatusHeader = self.listingStatus.locator('.PDPRightRailCard__ListingStatus')
        self.listingStatusMonthlyPayment = self.listingStatus.locator('[data-hc-name=monthly-payment]')
        self.listingStatusMortgageInfoButton = self.listingStatusMonthlyPayment.get_by_label('Toggle mortgage info')
        self.mortgageInfo = self.propertyOptionsPanel.locator('.PDPRightRailCard__MortgageInfo')
        self.mortgageInfoLabel = self.mortgageInfo.locator('[class$=__Label]')
        self.mortgageInfoValue = self.mortgageInfo.locator('[class$=__Value]')
        self.contactAgentButton = self.propertyOptionsPanel.locator('[data-hc-name=contact-agent-button]')
        self.requestTourButton = self.propertyOptionsPanel.get_by_label('Request tour')
        self.requestTourButtonLabel = self.propertyOptionsPanel.locator('.RequestATourButton__RequestATourButton > div[class$=__ButtonLabel]')
        self.saveButton = self.propertyOptionsPanel.get_by_label('Save this property to your Watchlist')
        self.saveButtonLabel = self.propertyOptionsPanel.locator('[data-hc-name=save-button] > div[class$=__ButtonLabel]')
        self.shareButton = self.propertyOptionsPanel.get_by_label('share')
        self.shareButtonLabel = self.propertyOptionsPanel.locator('[data-hc-name=share-button] > label')
        self.mlsAttribution = self.propertyOptionsPanel.locator('.PDPRightRailCard__MLSAttribution')
        # Property Intro Section
        self.propertyIntroSection = page.locator(selectors['propertyIntroSection'])
        self.propertyFullAddress = self.propertyIntroSection.locator('h1')
        self.propertyDetails = self.propertyIntroSection.locator('[data-hc-name=property-info]')
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
        self.zoomInButton = self.mapSection.locator('[data-hc-name=zoom in]')
        self.zoomOutButton = self.mapSection.locator('[data-hc-name=zoom out]')
        self.mapSectionInfoButton = self.mapSection.locator(selectors['mapSectionInfoButton'])
        # AVM Section
        self.avmSection = page.locator('[data-hc-name=avm-breakdown]')

        # AVM Breakout Section
        self.avmBreakoutSection = page.locator('[data-hc-name=avm-breakout-section]')

    # Methods
    def getUrl(self, slug):
        url = f"{BasePage.BASE_URL}property-details/{slug}"
        return url
    
    def getTitle(self, address):
        title = f"{address} | Property Details | ComeHome"
        return title
    
    def goto(self, slug):
        url = self.getUrl(slug)
        self.page.goto(url)
    
    def getPropertyPageDetails(self, data):
        res = {}
        res['full_address'] = self.constructFullAddress(data)
        res['slug'] = self.constructSlug(data)
        return res
    
    def getPropertyDetailsData(self):
        res = {}
        label = self.propertyDetailsRow.locator('th')
        value = self.propertyDetailsRow.locator('td')
        for row in range(self.propertyDetailsRow.count()):
            res[label.nth(row).text_content()] = value.nth(row).text_content()
        return res
    
    def getMortgageData(self):
        res = {}
        for info in range(self.mortgageInfoLabel.count()):
            res[self.mortgageInfoLabel.nth(info).text_content()] = self.mortgageInfoValue.nth(info).text_content()
        return res
