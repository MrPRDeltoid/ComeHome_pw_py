import json
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

        # Load in common selectors from json file
        with open(r".\common\selectors.json", mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['alerts_page']

        # Header Section
        self.headerSection = self.page.locator(selectors['headerSection'])

        # Logged Out Section
        self.loggedOutSection = self.page.locator(selectors['loggedOutSection'])

    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
