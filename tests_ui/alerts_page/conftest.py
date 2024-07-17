import pytest
from pages.alerts_page import AlertsPage


@pytest.fixture()
def setup_alerts_page(alerts_page: AlertsPage, setup):
    alerts_page.goto()
