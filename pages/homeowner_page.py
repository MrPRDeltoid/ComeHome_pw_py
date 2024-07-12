from playwright.sync_api import Page
from .base_page import BasePage


class HomeownerPage(BasePage):
    """Locators and methods for the Homeowner Page"""
    URL = f"{BasePage.BASE_URL}homeowner"
    TITLE = "My Home | ComeHome"

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
