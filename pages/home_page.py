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
        self.photoColumn = self.photoSection.locator('class$="__PhotoColumn"]');
        self.photo = self.photoSection.locator('[class$="__PhotoColumnPhoto"]');
        # Track or Buy Section
        self.trackOrBuySection = page.locator('[class$="__HomeSubpageTrackOrBuyHome"]')
        self.buyHomeTitle = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-header"]')
        self.buyHomeDescription = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-description"]')
        self.searchHomesButton = self.trackOrBuySection.locator('[data-hc-name="buy-home-modal-button"]')
        self.yourHomeTitle = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-header"]')
        self.yourHomeDescription = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-description"]')
        self.seeMyHomeButton = self.trackOrBuySection.locator('[data-hc-name="your-home-dash-modal-button"]')
        # Team Agent Section
        self.yourTeamAgentSection = page.locator('[class$="__HomeSubpageYourTeamAgent"]')
        self.findAgentTitle = self.yourTeamAgentSection.locator('.HomeSubpageYourTeamAgent__CardHeader')
        self.findAgentDescription = self.yourTeamAgentSection.locator('.HomeSubpageYourTeamAgent__CardDescription')
        self.findAgentButton = self.yourTeamAgentSection.locator('[data-hc-name="find-an-agent-cta"]')

    # Methods
    def goto(self):
        self.page.goto(self.URL)
