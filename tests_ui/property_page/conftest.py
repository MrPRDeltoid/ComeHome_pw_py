import pytest
from pages.property_page import PropertyPage


@pytest.fixture
def setup_property_page(property_page: PropertyPage, setup):
    def _setup(slug):
        property_page.goto(slug)
    yield _setup
