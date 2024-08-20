from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage
from pages.search_page import SearchPage


def verify_dropdown_options(options, exp_options):
    for option in range(options.count()):
        option_text = options.nth(option).text_content()
        assert option_text == exp_options[option]
    options.nth(0).click()

def test_search_property(page: Page, property_page: PropertyPage, search_page: SearchPage, setup_search_page):
    """Enter valid property in field, verify correct search results and clicking result loads correct property page"""
    property_data = search_page.get_property_data('property1')
    full_address = search_page.construct_full_address(property_data)
    slug = search_page.construct_slug(property_data)
    search_page.searchInput.fill(property_data['street'])
    expect(search_page.searchResults).to_be_visible()
    expect(search_page.searchResults.get_by_role('heading')).to_have_text('Address')
    expect(search_page.searchResults.get_by_role('option').first).to_have_text(full_address)
    expect(search_page.searchResults.get_by_role('option').last).to_have_text("Can't find your address?")
    # Click the search result to load property page
    search_page.searchResults.get_by_role('option').first.click()
    expect(page).to_have_url(property_page.get_url(slug))
    expect(page).to_have_title(property_page.get_title(full_address))

def test_price_filter_menu(search_page: SearchPage, setup_search_page):
    """Click the Price filter button and verify menu options"""
    exp_price_options = ['$50,000', '$75,000', '$100,000', '$150,000', '$200,000', '$250,000', '$300,000',
                         '$350,000', '$400,000', '$450,000', '$500,000', '$600,000', '$700,000', '$800,000',
                         '$900,000', '$1,000,000', '$1,500,000', '$2,000,000', '$2,500,000', '$3,000,000',
                         '$3,500,000', '$4,000,000', '$4,500,000', '$5,000,000', '$6,000,000', '$7,000,000',
                         '$8,000,000', '$9,000,000', '$10,000,000']
    expect(search_page.priceButton).to_have_text('Price: Any')
    search_page.priceButton.click()
    expect(search_page.priceMenu).to_be_visible()
    expect(search_page.priceMenu.locator('[id^=left-label-]')).to_have_text('Min Price')
    expect(search_page.priceMenu.locator('.SearchTopBarFilters__DropdownRangeMin')).to_have_text('No Min')
    expect(search_page.priceMenu.locator('[id^=right-label-]')).to_have_text('Max Price')
    expect(search_page.priceMenu.locator('.SearchTopBarFilters__DropdownRangeMax')).to_have_text('No Max')
    # Click the min/max dropdowns to verify options
    search_page.priceMenu.locator('.SearchTopBarFilters__DropdownRangeMin').get_by_role('button').click()
    exp_price_options.insert(0, "No Min")
    min_options = search_page.priceMenu.get_by_role('listbox').get_by_role('option')
    verify_dropdown_options(min_options, exp_price_options)
    search_page.priceMenu.locator('.SearchTopBarFilters__DropdownRangeMax').get_by_role('button').click()
    exp_price_options[0] = 'No Max'
    max_options = search_page.priceMenu.get_by_role('listbox').get_by_role('option')
    verify_dropdown_options(max_options, exp_price_options)