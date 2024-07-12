from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_correct_text_and_elements_find_view(home_page: HomePage, setup):
    """Given Find a home is selectyed, verify top section has correct header text and elements"""
    expect(home_page.header).to_have_text("Find your dream home")
    expect(home_page.subheader).to_have_text("Search homes in your neighborhood and find a house that's right for you.")
    expect(home_page.findHomeButton).to_have_text("Find a home")
    expect(home_page.findHomeButton).to_have_attribute('data-state', 'active')
    expect(home_page.trackHomeButton).to_have_text("My home value")
    expect(home_page.trackHomeButton).to_have_attribute('data-state', 'inactive')
    expect(home_page.searchField).to_have_attribute('placeholder', "Search for a city, ZIP code or address")
    expect(home_page.searchButton).to_be_visible()

def test_correct_text_and_elements_track_view(home_page: HomePage, setup):
    """Given My home value is selected, verify top section has correct header text and elements"""
    home_page.trackHomeButton.click()
    expect(home_page.header).to_have_text("See your home's full potential")
    expect(home_page.subheader).to_have_text("Claim your home and unlock features to see your home's value, equity, and more.")
    expect(home_page.findHomeButton).to_have_text("Find a home")
    expect(home_page.findHomeButton).to_have_attribute('data-state', 'inactive')
    expect(home_page.trackHomeButton).to_have_text("My home value")
    expect(home_page.trackHomeButton).to_have_attribute('data-state', 'active')
    expect(home_page.searchField).to_have_attribute('placeholder', "Enter your home address")
    expect(home_page.searchButton).to_be_visible()
