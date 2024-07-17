from playwright.sync_api import Page
from .base_page import BasePage


class AgentPage(BasePage):
    """Locators and methods for the Agent Page"""
    URL = f"{BasePage.BASE_URL}concierge-team"
    TITLE = "Find an Agent | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
