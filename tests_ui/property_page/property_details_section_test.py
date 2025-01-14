from datetime import date
from playwright.sync_api import expect
from pages.property_page import PropertyPage


def test_property_details_section_test(property_page: PropertyPage, setup_property_page):
    """Check Property Details Section has correct caption, data, and attribution"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])

    expect(property_page.propertyDetailsCaption).to_have_text("Additional home details")
    exp_property_details = {'Living Area': f'{property_data['gla']} Sq.Ft.',
                            'Lot Size': f'{property_data['lot_size']} Sq.Ft.',
                            'Total Rooms': '--', 
                            'Bedrooms': str(property_data['beds']),
                            'Bathrooms': str(property_data['baths']),
                            'Stories': '1',
                            'Year Built': property_data['year_built'],
                            'Property Type': property_data['type'],
                            'Zoning': 'PSR6',
                            'HOA Name': '--',
                            'HOA Fee': '--',
                            'HOA Includes': '--',
                            'Tax Year': str(date.today().year - 1),  # Last year should be latest tax year
                            'Tax Amount': '',
                            'Property in Flood Zone': '--'}
    property_details = property_page.getPropertyDetailsData()
    property_details['Tax Amount'] = ''  # Tax amount can change, just check that the entry exists
    assert property_details == exp_property_details
    expect(property_page.propertyDetailsAttribution).to_have_text("Data provided by CRMLS.")
