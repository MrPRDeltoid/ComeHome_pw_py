from playwright.sync_api import expect
from pages.property_page import PropertyPage


def test_intro_section_text(property_page: PropertyPage, setup_property_page):
    """Check Intro Section has correct address and details"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])

    expect(property_page.propertyFullAddress).to_have_text(F"{property_data['street']}., {property_data['city']}, {property_data['state']} {property_data['zip']}")
    expect(property_page.propertyDetails).to_have_text(f"{property_data['type']}{property_data['beds']} Beds{property_data['baths']} Baths{property_data['gla']} Sq Ft")
