import pytest
from pages.watchlist_page import WatchlistPage


@pytest.fixture()
def setup_watchlist_page(watchlist_page: WatchlistPage, setup):
    watchlist_page.goto()
