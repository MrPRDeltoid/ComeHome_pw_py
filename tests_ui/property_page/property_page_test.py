from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage


def test_top_bar_text_and_elements(page: Page, property_page: PropertyPage, setup_property_page):
    """Check correct url, title and all main sections are shown"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])
    expect(page).to_have_url(property_page.getUrl(property_details['slug']))
    expect(page).to_have_title(property_page.getTitle(property_details['full_address']))
    expect(property_page.mainMenu).to_be_visible()
    expect(property_page.topBar).to_be_visible()
    expect(property_page.photoSection).to_be_visible()
    expect(property_page.propertyOptionsPanel).to_be_visible()
    expect(property_page.brokerageSection).to_have_count(2)  # Seperate element for mobile view
    expect(property_page.propertyIntroSection).to_be_visible()
    expect(property_page.propertyDetailsSection).to_be_visible()
    expect(property_page.claimHomeSection).to_be_visible()
    expect(property_page.mapSection).to_be_visible()
    expect(property_page.avmSection).to_be_visible()
    expect(property_page.avmBreakoutSection).to_be_visible()
    expect(property_page.footerSection).to_be_visible()
