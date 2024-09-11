from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


def verify_min_max_dropdown_options(search_page: SearchPage, filter, row, exp_options: list):
    min_dropdown = search_page.filterRow.nth(row).locator(search_page.filter_dropdown_min)
    max_dropdown = search_page.filterRow.nth(row).locator(search_page.filter_dropdown_max)
    expect(min_dropdown).to_have_text('No Min')
    expect(max_dropdown).to_have_text('No Max')
    # Click to open min dropdown and verify options
    min_dropdown.get_by_role('button').click()
    if filter == "Year Built":
        exp_options.append('No Min')
    else:
        exp_options.insert(0, 'No Min')
    min_options = min_dropdown.get_by_role('listbox').get_by_role('option')
    expect(min_options).to_have_count(len(exp_options))
    expect(min_options).to_have_text(exp_options)
    min_options.get_by_text('No Min').click()
    # Click to open max dropdown and verify options
    max_dropdown.get_by_role('button').click()
    if filter == "Year Built":
        exp_options[-1] = 'No Max'
    else:
        exp_options[0] = 'No Max'
    max_options = max_dropdown.get_by_role('listbox').get_by_role('option')
    expect(max_options).to_have_count(len(exp_options))
    expect(max_options).to_have_text(exp_options)
    max_options.get_by_text('No Max').click()

def test_more_filters_menu(search_page: SearchPage, setup_search_page):
    """Click the More filters button and verify menu contents"""
    expect(search_page.moreFiltersButton).to_have_text('More Filters(1)')
    search_page.moreFiltersButton.click()
    expect(search_page.moreFiltersMenu).to_be_visible()
    expect(search_page.clearFiltersButton).to_have_text('Clear All Filters')
    exp_filter_labels = ['Listing Status', 'Price', 'Property Type', 'Beds', 'Baths', 'ComeHome Value', 'Square Feet',
                         'Price per Square Foot', 'Lot Size', 'Days on Market', 'Year Built', 'One-Year Forecast', 'Crime',
                         'Elementary', 'Middle', 'High']
    for row in range(search_page.filterRow.count()):
        filter_label = search_page.filterRowLabel.nth(row)
        expect(filter_label).to_have_text(exp_filter_labels[row])
        filter_name = filter_label.text_content()
        if filter_name == "Listing Status":
            checkboxes = search_page.filterRowControl.nth(row).get_by_role('checkbox')
            labels = search_page.filterRowControl.nth(row).locator('label')
            assert search_page.getFilterCheckboxSettings(checkboxes, labels) == {'For sale': True,
                                                                                    'Off Market': False,
                                                                                    'Pending': False,
                                                                                    'Under Contract': False,
                                                                                    'All': False}
        if filter_name in ["Price", "ComeHome Value", "Square Feet", "Price per Square Foot", "Lot Size", "Year Built"]:
            if filter_name in ["Price", "ComeHome Value"]:
                exp_options = list(search_page.PRICE_FILTER_OPTIONS)
                verify_min_max_dropdown_options(search_page, filter_name, row, exp_options)
            elif filter_name == "Square Feet":
                exp_options = list(search_page.SQUARE_FEET_FILTER_OPTIONS)
                verify_min_max_dropdown_options(search_page, filter_name, row, exp_options)
            elif filter_name == "Price per Square Foot":
                exp_options = list(search_page.PRICE_PER_SQFT_FILTER_OPTIONS)
                verify_min_max_dropdown_options(search_page, filter_name, row, exp_options)
            elif filter_name == "Lot Size":
                exp_options = list(search_page.LOT_SIZE_FILTER_OPTIONS)
                verify_min_max_dropdown_options(search_page, filter_name, row, exp_options)
            elif filter_name == "Year Built":
                exp_options = list(search_page.YEAR_BUILT_FILTER_OPTIONS)
                verify_min_max_dropdown_options(search_page, filter_name, row, exp_options)
        if filter_name == "Property Type":
            checkboxes = search_page.filterRowControl.nth(row).get_by_role('checkbox')
            labels = search_page.filterRowControl.nth(row).locator('label')
            assert search_page.getFilterCheckboxSettings(checkboxes, labels) == {'House': False,
                                                                                    'Townhouse': False,
                                                                                    'Condo': False,
                                                                                    'Co-op': False,
                                                                                    'All': True}
        if filter_name in ['Beds', 'Baths']:
            expect(search_page.filterRow.nth(row).get_by_role('button').first).to_have_text('-')
            expect(search_page.filterRow.nth(row).get_by_role('button').first).to_be_disabled()
            expect(search_page.filterRow.nth(row).locator('.NumberAdjuster__NumberAdjusterControls').locator('.NumberAdjuster__ValueLabel')).to_have_text('0+')
            expect(search_page.filterRow.nth(row).get_by_role('button').last).to_have_text('+')
            expect(search_page.filterRow.nth(row).get_by_role('button').last).to_be_enabled()
        if filter_name == "Days on Market":
            dropdown = search_page.filterRow.nth(row).get_by_role('button')
            expect(dropdown).to_have_text('Any')
            dropdown.click()
            options = search_page.filterRow.nth(row).get_by_role('listbox').get_by_role('option')
            expect(options).to_have_text(search_page.DAYS_ON_MARKET_FILTER_OPTIONS)
            options.get_by_text('Any').click()
        if filter_name == "One-Year Forecast":
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).first).to_have_text('-10%')
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).last).to_have_text('20%')
        if filter_name == "Crime":
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).first).to_have_text('Lowest')
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).last).to_have_text('Highest')
        expect(search_page.schoolsFilterTitle).to_have_text("Schools")
        if filter_name in ["Elementary", "Middle", "High"]:
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).first).to_have_text('0%')
            expect(search_page.filterRow.nth(row).locator(search_page.filter_slider_value).last).to_have_text('100%')
    expect(search_page.searchByMLSNumberLink).to_have_attribute('href', '/mls-number')
    expect(search_page.showAdvancedFiltersButton).to_have_text('Show Advanced Filters')
    expect(search_page.showAdvancedFiltersButton).to_have_attribute('aria-expanded', 'false')
    search_page.showAdvancedFiltersButton.click()
    expect(search_page.showAdvancedFiltersButton).to_have_text('Hide')
    search_page.showAdvancedFiltersButton.click()
    expect(search_page.showAdvancedFiltersButton).to_have_text('Show Advanced Filters')
