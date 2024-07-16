from playwright.sync_api import Page
from .base_page import BasePage


class PropertyPage(BasePage):
    """Locators and methods for the Property Page"""
    def get_url(self, slug):
        URL = f"{BasePage.BASE_URL}property-details/{slug}"
        return URL
    
    def get_title(self, address):
        TITLE = f"{address} | Property Details | ComeHome"
        return TITLE

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
