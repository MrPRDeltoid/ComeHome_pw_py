import json
from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage


def test_top_bar_text_and_elements(page: Page, property_page: PropertyPage, setup_property_page):
    """Check top bar address and view buttons"""
    with open(r".\.\data\properties.json", mode="r", encoding="utf-8") as data_file:
        property_data = json.load(data_file)['property1']
    full_address = property_page.construct_full_address(property_data)
    slug = property_page.construct_slug(property_data)
    setup_property_page(slug)

    expect(page).to_have_url(property_page.get_url(slug))
    expect(page).to_have_title(property_page.get_title(full_address))
    expect(property_page.breadcrumbs).to_have_text(f"Home{property_data['city']}, {property_data['state']}{property_data['zip']}{property_data['street']}")
    expect(property_page.publicViewButton).to_have_text("Currently showingPublic view")
    expect(property_page.publicViewButton).to_have_attribute('data-state', 'active')
    expect(property_page.ownerViewButton).to_have_text("Owner view")
    expect(property_page.ownerViewButton).to_have_attribute('data-state', 'inactive')
