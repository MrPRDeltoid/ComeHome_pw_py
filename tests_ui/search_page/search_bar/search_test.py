from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage
from pages.search_page import SearchPage


def test_search_property(page: Page, property_page: PropertyPage, search_page: SearchPage, setup_search_page):
    """Enter valid property in field, verify correct search results and clicking result loads correct property page"""
    property_data = search_page.getPropertyData('property1')
    full_address = search_page.constructFullAddress(property_data)
    slug = search_page.constructSlug(property_data)
    search_page.searchInput.fill(property_data['street'])
    expect(search_page.searchResults).to_be_visible()
    expect(search_page.searchResults.get_by_role('heading')).to_have_text('Address')
    expect(search_page.searchResults.get_by_role('option').first).to_have_text(full_address)
    expect(search_page.searchResults.get_by_role('option').last).to_have_text("Can't find your address?")
    # Click the search result to load property page
    search_page.searchResults.get_by_role('option').first.click()
    expect(page).to_have_url(property_page.getUrl(slug))
    expect(page).to_have_title(property_page.getTitle(full_address))
