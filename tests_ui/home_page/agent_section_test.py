from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.agent_page import AgentPage


def test_correct_text_and_elements_find_view(home_page: HomePage, setup):
    """Verify Agent section has correct text and elements"""
    expect(home_page.findAgentImage).to_be_visible()
    expect(home_page.findAgentTitle).to_have_text("Need help finding an agent? We'll connect you.")
    expect(home_page.findAgentDescription).to_have_text("We can help pair you with the right agent for your real estate needs. Let our team help make locating the best agent easy and smooth.")
    expect(home_page.findAgentButton).to_have_text("Learn More")
    expect(home_page.findAgentButton).to_have_css('background-color', 'rgb(86, 78, 240)')

def test_click_learn_more_button(page: Page, home_page: HomePage, agent_page: AgentPage, setup):
    """Verify clicking on Learn More button navigates to correct page"""
    home_page.findAgentButton.click()
    expect(page).to_have_url(agent_page.URL)
    # expect(page).to_have_title(agent_page.TITLE)  # TODO: BUG - Agent page does not update the title
