from playwright.sync_api import Page, expect
from pages.property_page import PropertyPage
from pages.search_page import SearchPage


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
    exp_price_options = list(search_page.PRICE_FILTER_OPTIONS)
    expect(search_page.priceButton).to_have_text('Price: Any')
    search_page.priceButton.click()
    expect(search_page.priceMenu).to_be_visible()
    expect(search_page.priceMinLabel).to_have_text('Min Price')
    expect(search_page.priceMinDropdown).to_have_text('No Min')
    expect(search_page.priceMaxLabel).to_have_text('Max Price')
    expect(search_page.priceMaxDropdown).to_have_text('No Max')
    # Click the min/max dropdowns to verify options
    search_page.priceMinDropdown.get_by_role('button').click()
    exp_price_options.insert(0, "No Min")
    min_options = search_page.priceMenu.get_by_role('listbox').get_by_role('option')
    assert search_page.get_filter_dropdown_options(min_options) == exp_price_options
    search_page.priceMaxDropdown.get_by_role('button').click()
    exp_price_options[0] = 'No Max'
    max_options = search_page.priceMenu.get_by_role('listbox').get_by_role('option')
    assert search_page.get_filter_dropdown_options(max_options) == exp_price_options

def test_property_type_filter_menu(search_page: SearchPage, setup_search_page):
    """Click the Property Type filter button and verify menu options"""
    expect(search_page.propertyTypeButton).to_have_text('Property Type: All')
    search_page.propertyTypeButton.click()
    expect(search_page.propertyTypeMenu).to_be_visible()
    checkboxes = search_page.propertyTypeMenu.get_by_role('checkbox')
    labels = search_page.propertyTypeCheckbox.locator('label')
    # Verify correct labels and default check state for each checkbox
    assert search_page.get_filter_checkbox_settings(checkboxes, labels) == {'House': False,
                                                                            'Townhouse': False,
                                                                            'Condo': False,
                                                                            'Co-op': False,
                                                                            'All': True}

def test_beds_filter_menu(search_page: SearchPage, setup_search_page):
    """Click the Beds filter button and verify menu contents"""
    expect(search_page.bedsButton).to_have_text('Beds: Any')
    search_page.bedsButton.click()
    expect(search_page.bedsMenu).to_be_visible()
    expect(search_page.bedsMenuButton.first).to_have_text('-')
    expect(search_page.bedsMenuButton.first).to_be_disabled()
    expect(search_page.bedsMenuLabel).to_have_text('0+')
    expect(search_page.bedsMenuButton.last).to_have_text('+')
    expect(search_page.bedsMenuButton.last).to_be_enabled()

def test_more_filters_menu(search_page: SearchPage, setup_search_page):
    """ Click the More filters button and verify menu contents"""
    expect(search_page.moreFiltersButton).to_have_text('More Filters(1)')
    search_page.moreFiltersButton.click()
    expect(search_page.moreFiltersMenu).to_be_visible()
    expect(search_page.clearFiltersButton).to_have_text('Clear All Filters')
    exp_filter_labels = ['Listing Status', 'Price', 'Property Type', 'Beds', 'Baths', 'ComeHome Value', 'Square Feet',
                         'Price per Square Foot', 'Lot Size', 'Days on Market', 'Year Built', 'One-Year Forecast', 'Crime']
    for row in range(search_page.filterRow.count() - 3):
        filter_label = search_page.filterRowLabel.nth(row)
        expect(filter_label).to_have_text(exp_filter_labels[row])
        if filter_label.text_content() == "Listing Status":
            checkboxes = search_page.filterRowControl.nth(row).get_by_role('checkbox')
            labels = search_page.filterRowControl.nth(row).locator('label')
            assert search_page.get_filter_checkbox_settings(checkboxes, labels) == {'For sale': True,
                                                                                    'Off Market': False,
                                                                                    'Pending': False,
                                                                                    'Under Contract': False,
                                                                                    'All': False}
        if filter_label.text_content() == "Price":
            exp_price_options = list(search_page.PRICE_FILTER_OPTIONS)
            min_dropdown = search_page.filterRow.nth(row).locator(search_page.filter_dropdown_min)
            max_dropdown = search_page.filterRow.nth(row).locator(search_page.filter_dropdown_max)
            expect(min_dropdown).to_have_text('No Min')
            expect(max_dropdown).to_have_text('No Max')
            min_dropdown.get_by_role('button').click()
            exp_price_options.insert(0, 'No Min')
            min_options = search_page.filterRow.nth(row).get_by_role('listbox').get_by_role('option')
            assert search_page.get_filter_dropdown_options(min_options) == exp_price_options
            max_dropdown.get_by_role('button').click()
            exp_price_options[0] = 'No Max'
            max_options = search_page.filterRow.nth(row).get_by_role('listbox').get_by_role('option')
            assert search_page.get_filter_dropdown_options(max_options) == exp_price_options
        if filter_label.text_content() == "Property Type":
            checkboxes = search_page.filterRowControl.nth(row).get_by_role('checkbox')
            labels = search_page.filterRowControl.nth(row).locator('label')
            assert search_page.get_filter_checkbox_settings(checkboxes, labels) == {'House': False,
                                                                                    'Townhouse': False,
                                                                                    'Condo': False,
                                                                                    'Co-op': False,
                                                                                    'All': True}
        if filter_label.text_content() in ['Beds', 'Baths']:
            expect(search_page.filterRow.nth(row).get_by_role('button').first).to_have_text('-')
            expect(search_page.filterRow.nth(row).get_by_role('button').first).to_be_disabled()
            expect(search_page.filterRow.nth(row).locator('.NumberAdjuster__NumberAdjusterControls').locator('.NumberAdjuster__ValueLabel')).to_have_text('0+')
            expect(search_page.filterRow.nth(row).get_by_role('button').last).to_have_text('+')
            expect(search_page.filterRow.nth(row).get_by_role('button').last).to_be_enabled()
    expect(search_page.searchByMLSNumberLink).to_have_attribute('href', '/mls-number')
    expect(search_page.showAdvancedFiltersButton).to_have_text('Show Advanced Filters')
    expect(search_page.showAdvancedFiltersButton).to_have_attribute('aria-expanded', 'false')
