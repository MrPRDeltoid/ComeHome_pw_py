from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.homeowner_page import HomeownerPage
from time import sleep


def test_correct_text_and_elements_find_view(home_page: HomePage, setup):
    """Verify Track or Buy Home section has correct text and elements"""
    expect(home_page.buyHomeImage).to_be_visible()
    expect(home_page.buyHomeTitle).to_have_text("Buying a home")
    expect(home_page.buyHomeDescription).to_have_text("Search homes for sale and filter by price, neighborhood, school ratings, and more. Find the perfect home that fits your needs.")
    expect(home_page.searchHomesButton).to_have_text("Search homes")
    expect(home_page.searchHomesButton).to_have_css('background-color', 'rgb(86, 78, 240)')
    expect(home_page.yourHomeImage).to_be_visible()
    expect(home_page.yourHomeTitle).to_have_text("Your homeowner dashboard")
    expect(home_page.yourHomeDescription).to_have_text("See your home's value, equity, and what a home renovation would do to your value. Claim your home and access these features and more.")
    expect(home_page.seeMyHomeButton).to_have_text("See my home")
    expect(home_page.seeMyHomeButton).to_have_css('background-color', 'rgb(86, 78, 240)')

def test_click_search_homes_button(page: Page, home_page: HomePage, search_page: SearchPage, setup):
    """Verify clicking on Search homes button navigates to correct page"""
    home_page.searchHomesButton.scroll_into_view_if_needed()
    sleep(0.5)  # TODO: Work around for animation making button unstable. See: https://github.com/microsoft/playwright/issues/15195
    home_page.searchHomesButton.click()
    expect(page).to_have_url(search_page.URL)
    expect(page).to_have_title(search_page.TITLE)

def test_click_see_home_button(page: Page, home_page: HomePage, homeowner_page: HomeownerPage, setup):
    """Verify clicking on See my home button navigates to correct page"""
    home_page.seeMyHomeButton.click()
    expect(page).to_have_url(homeowner_page.URL)
    expect(page).to_have_title(homeowner_page.TITLE)
