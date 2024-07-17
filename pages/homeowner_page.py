from playwright.sync_api import Page
from .base_page import BasePage


class HomeownerPage(BasePage):
    """Locators and methods for the Homeowner Page"""
    URL = f"{BasePage.BASE_URL}homeowner"
    TITLE = "My Home | ComeHome"

    def get_url_property(self, slug):
        """Given the slug, get the URL when a property is loaded in the Homowner page"""
        URL = f"{BasePage.BASE_URL}homeowner/{slug}"
        return URL
    
    def get_title_property(self, address):
        """Given the full address, get the Title when a property is loaded in the Homowner page"""
        TITLE = f"{address} | My Home | ComeHome"
        return TITLE

    # Locators
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Methods
    def goto(self):
        self.page.goto(self.URL)
