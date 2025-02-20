import re
from playwright.sync_api import expect
from pages.property_page import PropertyPage


def test_listing_status_section(property_page: PropertyPage, setup_property_page):
    """Check Listing Status info is correct and click to expand"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])

    expect(property_page.listingStatusHeader).to_contain_text("Off Market $")
    expect(property_page.listingStatusMonthlyPayment).to_contain_text("Estimated monthly payment $")
    expect(property_page.listingStatusMortgageInfoButton).to_have_attribute('aria-expanded', 'false')
    expect(property_page.mortgageInfo).to_be_hidden()
    # Click the mortgage info button to expand
    property_page.listingStatusMortgageInfoButton.click()
    expect(property_page.mortgageInfo).to_be_visible()
    expect(property_page.mortgageInfoValue.nth(3)).to_contain_text('$', timeout=10000)
    mortgage_data = property_page.getMortgageData()
    assert mortgage_data['Year fixed'] == "30"
    assert '%' in mortgage_data['Rate']
    monthly_total = int(property_page.listingStatusMonthlyPayment.text_content().split('$')[1].replace(',', ''))
    monthly_payment = int(mortgage_data['Mortgage Payment'].replace('$', '').replace(',', ''))
    monthly_taxes = int(mortgage_data['Property taxes'].replace('$', '').replace(',', ''))
    assert monthly_total - 1 <= monthly_payment + monthly_taxes <= monthly_total + 1  # To handle any rounding issues
    assert mortgage_data['Insurance'] == '--'
    assert mortgage_data['HOA fees'] == '--'
    # Click to hide mortgage info
    property_page.listingStatusMortgageInfoButton.click()
    expect(property_page.mortgageInfo).to_be_hidden()
    expect(property_page.contactAgentButton).to_be_enabled()
    expect(property_page.contactAgentButton).to_have_text("Contact Agent")
    expect(property_page.requestTourButton).to_be_enabled()
    expect(property_page.requestTourButtonLabel).to_have_text("Request tour")
    expect(property_page.shareButton).to_be_enabled()
    expect(property_page.shareButtonLabel).to_have_text("Share")
    expect(property_page.saveButton).to_be_enabled()
    expect(property_page.saveButtonLabel).to_have_text("Save")
    expect(property_page.mlsAttribution).to_have_text("Courtesy of RE/MAX Gold Coast REALTORS")
