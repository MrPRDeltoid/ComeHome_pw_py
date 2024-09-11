from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage
from pages.homeowner_page import HomeownerPage


def test_top_bar_text_and_elements(page: Page, property_page: PropertyPage, setup_property_page):
    """Check top bar address and view buttons"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])
    expect(page).to_have_url(property_page.getUrl(property_details['slug']))
    expect(page).to_have_title(property_page.getTitle(property_details['full_address']))
    expect(property_page.breadcrumbs).to_have_text(f"Home{property_data['city']}, {property_data['state']}{property_data['zip']}{property_data['street']}")
    expect(property_page.publicViewButton).to_have_text("Currently showingPublic view")
    expect(property_page.publicViewButton).to_have_attribute('data-state', 'active')
    expect(property_page.ownerViewButton).to_have_text("Owner view")
    expect(property_page.ownerViewButton).to_have_attribute('data-state', 'inactive')

def test_top_bar_view_toggle(page: Page, property_page: PropertyPage, homeowner_page: HomeownerPage, setup_property_page):
    """Check that clicking Public/Owner toggle buttons shows correct views"""
    property_data = property_page.getPropertyData('property1')
    property_details = property_page.getPropertyPageDetails(property_data)
    setup_property_page(property_details['slug'])
    # Click Owner View toggle
    property_page.ownerViewButton.click()
    expect(page).to_have_url(homeowner_page.getUrlProperty(property_details['slug']))
    expect(page).to_have_title(homeowner_page.getTitleProperty(property_details['full_address']))
    expect(homeowner_page.publicViewButton).to_have_attribute('data-state', 'inactive')
    expect(homeowner_page.ownerViewButton).to_have_attribute('data-state', 'active')
    # Click Public View toggle
    property_page.publicViewButton.click()
    expect(page).to_have_url(property_page.getUrl(property_details['slug']))
    expect(page).to_have_title(property_page.getTitle(property_details['full_address']))
    expect(property_page.publicViewButton).to_have_attribute('data-state', 'active')
    expect(property_page.ownerViewButton).to_have_attribute('data-state', 'inactive')
