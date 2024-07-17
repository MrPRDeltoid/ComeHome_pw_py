from playwright.sync_api import Page
from .base_page import BasePage


class HomePage(BasePage):
    """Locators and methods for the Home Page"""
    URL = BasePage.BASE_URL
    TITLE = "Home | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Top Section
        self.topSection = page.locator('[class$="__TopSection"]')
        self.header = self.topSection.locator('h1')
        self.subheader = self.topSection.locator('[class$="__SubHeader"]')
        self.findHomeButton = self.topSection.locator('[data-hc-name="find-a-home"]')
        self.trackHomeButton = self.topSection.locator('[data-hc-name="track-my-home"]')
        self.searchField = self.topSection.locator('[name^="comehome-address-search-"]')
        self.searchButton = self.topSection.locator('button[class$="HomeSubpageSearch__SearchButton"]')
        self.searchResultItem = self.topSection.locator('[data-hc-name="header-search-results-address-list-item"]')
        # Photo Section
        self.photoSection = page.locator('[class$="__PhotoSection"]')
        self.photoColumn = self.photoSection.locator('[class$="__PhotoColumn"]')
        self.photo = self.photoSection.locator('[class$="__PhotoColumnPhoto"]')
        # Track or Buy Section
        self.trackOrBuySection = page.locator('[class$="__HomeSubpageTrackOrBuyHome"]')
        self.buyHomeImage = self.trackOrBuySection.locator('img').and_(self.trackOrBuySection.get_by_alt_text("A building"))
        self.buyHomeTitle = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-header"]')
        self.buyHomeDescription = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-description"]')
        self.searchHomesButton = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-button"]')
        self.yourHomeImage = self.trackOrBuySection.locator('img').and_(self.trackOrBuySection.get_by_alt_text("A house"))
        self.yourHomeTitle = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-header"]')
        self.yourHomeDescription = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-description"]')
        self.seeMyHomeButton = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-button"]')
        # Agent Section
        self.agentSection = page.locator('[class$="__HomeSubpageYourTeamAgent"]')
        self.findAgentImage = self.agentSection.locator('img').and_(self.agentSection.get_by_alt_text("a hand writing with a pen"))
        self.findAgentTitle = self.agentSection.locator('.HomeSubpageYourTeamAgent__CardHeader')
        self.findAgentDescription = self.agentSection.locator('.HomeSubpageYourTeamAgent__CardDescription')
        self.findAgentButton = self.agentSection.locator('[data-hc-name="find-an-agent-cta"]')

    # Methods
    def goto(self):
        self.page.goto(self.URL)
    
    def search_for_property(self, property):
        self.searchField.fill(property)
        self.searchButton.click()
