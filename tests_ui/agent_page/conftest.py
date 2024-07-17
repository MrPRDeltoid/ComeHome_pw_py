import pytest
from pages.agent_page import AgentPage


@pytest.fixture()
def setup_agent_page(agent_page: AgentPage, setup):
    agent_page.goto()
