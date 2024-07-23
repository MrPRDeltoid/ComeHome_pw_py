import { test, expect } from '@playwright/test';
import { WatchlistPage } from '../pages/watchlist_page.js';
import { watch } from 'fs';


test.beforeEach('Load Watchlist Page', async ({ page }) => {
    const watchlist_page = new WatchlistPage(page);
  
    await watchlist_page.gotoWatchlistPage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Watchlist Page', () => {
    test('has expected sections', async ({ page }) => {
        const watchlist_page = new WatchlistPage(page);

        await expect(watchlist_page.mainMenu).toHaveScreenshot('watchlist_page_mainMenu.png');
        await expect(watchlist_page.headerSection).toHaveScreenshot('watchlist_page_headerSection.png');
        await expect(watchlist_page.loggedOutSection).toHaveScreenshot('watchlist_page_loggedOutSection.png');
        await expect(watchlist_page.footerSection).toHaveScreenshot('watchlist_page_footerSection.png');
    });
});
