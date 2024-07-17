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
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
