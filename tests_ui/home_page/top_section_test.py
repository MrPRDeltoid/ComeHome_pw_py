from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.property_page import PropertyPage
from pages.homeowner_page import HomeownerPage


def verify_text_and_elements(home_page: HomePage, exp_data):
    expect(home_page.header).to_have_text(exp_data['header'])
    expect(home_page.subheader).to_have_text(exp_data['subheader'])
    expect(home_page.findHomeButton).to_have_text("Find a home")
    expect(home_page.findHomeButton).to_have_attribute('data-state', exp_data['find_home_state'])
    expect(home_page.trackHomeButton).to_have_text("My home value")
    expect(home_page.trackHomeButton).to_have_attribute('data-state', exp_data['track_home_state'])
    expect(home_page.searchField).to_have_attribute('placeholder', exp_data['placeholder'])
    expect(home_page.searchButton).to_be_visible()

def test_correct_text_and_elements_find_view(home_page: HomePage, setup):
    """Given Find a home is selected, verify top section has correct header text and elements"""
    exp_data = {'header': "Find your dream home",
                'subheader': "Search homes in your neighborhood and find a house that's right for you.",
                'find_home_state': 'active',
                'track_home_state': 'inactive',
                'placeholder': "Search for a city, ZIP code or address"}
    verify_text_and_elements(home_page, exp_data)

def test_correct_text_and_elements_track_view(home_page: HomePage, setup):
    """Given My home value is selected, verify top section has correct header text and elements"""
    exp_data = {'header': "See your home's full potential",
                'subheader': "Claim your home and unlock features to see your home's value, equity, and more.",
                'find_home_state': 'inactive',
                'track_home_state': 'active',
                'placeholder': "Enter your home address"}
    home_page.trackHomeButton.click()
    verify_text_and_elements(home_page, exp_data)

def test_search_find_view(page: Page, home_page: HomePage, property_page: PropertyPage, setup):
    """Given Find a home is selected, enter existing property in search field to verify correct property page loads"""
    property_data = home_page.getPropertyData('property1')
    home_page.searchForProperty(property_data['street'])
    full_address = home_page.constructFullAddress(property_data)
    slug = home_page.constructSlug(property_data)
    expect(page).to_have_url(property_page.getUrl(slug))
    expect(page).to_have_title(property_page.getTitle(full_address))

def test_search_track_view(page: Page, home_page: HomePage, homeowner_page: HomeownerPage, setup):
    """Given My home value is selected, enter existing property in search field to verify correct homeowner page loads"""
    property_data = home_page.getPropertyData('property1')
    home_page.trackHomeButton.click()
    home_page.searchForProperty(property_data['street'])
    full_address = home_page.constructFullAddress(property_data)
    slug = home_page.constructSlug(property_data)
    expect(page).to_have_url(homeowner_page.getUrlProperty(slug))
    expect(page).to_have_title(homeowner_page.getTitleProperty(full_address))
