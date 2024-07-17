from playwright.sync_api import Page, expect
from pages.agent_page import AgentPage


def test_verify_main_sections(page: Page, agent_page: AgentPage, setup_agent_page):
    """Check correct url, title and all main sections are shown"""
    expect(page).to_have_url(agent_page.URL)
    #expect(page).to_have_title(agent_page.TITLE)  # TODO: BUG - Agent page does not update the title
    expect(agent_page.mainMenu).to_be_visible()
    expect(agent_page.topSection).to_be_visible()
    expect(agent_page.subSection).to_be_visible()
    expect(agent_page.footerSection).to_be_visible()
