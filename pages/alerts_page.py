from playwright.sync_api import Page
from .base_page import BasePage


class AlertsPage(BasePage):
    """Locators and methods for the Alerts Page"""
    URL = f"{BasePage.BASE_URL}alerts"
    TITLE = "Alerts | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Header Section
        self.headerSection = self.page.locator('.AlertsHeader__AlertsHeadingBox')

        # Logged Out Section
        self.loggedOutSection = self.page.locator('[data-hc-name="logged-out-section"]')

    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
