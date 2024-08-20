from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage
from pages.homeowner_page import HomeownerPage


def test_click_claim_home_button(page: Page, property_page: PropertyPage, homeowner_page: HomeownerPage, setup_property_page):
    """Click the Claim Home button and verify correct Homeowner Page is loaded"""
    property_data = property_page.get_property_data('property1')
    property_details = property_page.get_property_page_details(property_data)
    setup_property_page(property_details['slug'])

    property_page.claimHomeButton.click()
    expect(page).to_have_url(homeowner_page.get_url_property(property_details['slug']))
    expect(page).to_have_title(homeowner_page.get_title_property(property_details['full_address']))
    expect(homeowner_page.avmmSectionAddress).to_have_text(property_data['street'])
    expect(homeowner_page.avmSectionDetails).to_have_text(f"{property_data['beds']} Bed|{property_data['beds']} Bath|{property_data['gla'].replace(',', '')} Sq Ft.")