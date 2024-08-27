from playwright.sync_api import Page, expect
from pages.search_page import SearchPage


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
    expect(min_options).to_have_count(len(exp_price_options))
    expect(min_options).to_have_text(exp_price_options)
    min_options.get_by_text('No Min').click()
    search_page.priceMaxDropdown.get_by_role('button').click()
    exp_price_options[0] = 'No Max'
    max_options = search_page.priceMenu.get_by_role('listbox').get_by_role('option')
    expect(max_options).to_have_count(len(exp_price_options))
    expect(max_options).to_have_text(exp_price_options)
    max_options.get_by_text('No Max').click()
