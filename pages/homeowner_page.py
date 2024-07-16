from playwright.sync_api import Page
from .base_page import BasePage


class HomeownerPage(BasePage):
    """Locators and methods for the Homeowner Page"""
    def get_url(self, slug):
        URL = f"{BasePage.BASE_URL}homeowner/{slug}"
        return URL
    
    def get_title(self, address):
        TITLE = f"{address} | My Home | ComeHome"
        return TITLE

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
