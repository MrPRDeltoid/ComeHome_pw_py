from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def test_property_section_elements(search_page: SearchPage, setup_search_page):
    """Check correct elements in Property Section"""
    expect(search_page.brokerageSection.last).to_be_visible()
    expect(search_page.sortButton).to_have_text('Sort')
    expect(search_page.propertyCount).to_contain_text(' Results')
    for idx in [7, 10, 16, 22, 28, 34, 39]:  # TODO: Better way to overcome lazy loading?
        search_page.propertyCard.nth(idx).scroll_into_view_if_needed()
    expect(search_page.propertyCard).to_have_count(40)
    expect(search_page.loadMoreResultsButton).to_have_text('Load More Results')
    expect(search_page.footerSection).to_be_visible()
