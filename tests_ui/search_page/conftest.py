import pytest
from playwright.sync_api import BrowserContext
from pages.search_page import SearchPage


@pytest.fixture()
def setup_search_page(context: BrowserContext, search_page: SearchPage, setup):
    # Need to set geolocation and grant permission to suppress the location request popup
    context.set_geolocation(geolocation={"latitude": 37.773972, "longitude": -122.431297})
    context.grant_permissions(permissions=['geolocation'])
    search_page.goto()
