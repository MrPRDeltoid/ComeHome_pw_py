import pytest
from pages.homeowner_page import HomeownerPage


@pytest.fixture()
def setup_homeowner_page(homeowner_page: HomeownerPage, setup):
    homeowner_page.goto()
