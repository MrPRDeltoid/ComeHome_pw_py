import json
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

        # Load in common selectors from json file
        with open(BasePage.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['agent_page']

        # Top Section
        self.topSection = self.page.locator(selectors['topSection'])

        # Sub Section
        self.subSection = self.page.locator(selectors['subSection'])
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
