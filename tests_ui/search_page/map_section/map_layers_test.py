from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_layers_bar(search_page: SearchPage, setup_search_page):
    """Verify the layers bar contents"""
    exp_layers = ['Crime', 'Schools', 'Price', 'Forecast']
    expect(search_page.layerButtons).to_have_count(4)
    for button in range(search_page.layerButtons.count()):
        expect(search_page.layerButtons.nth(button)).to_have_text(exp_layers[button])
