import { test, expect } from '@playwright/test';
import { SearchPage } from '../pages/search_page.js';


test.beforeEach('Load Search Page', async ({ page }) => {
    const search_page = new SearchPage(page);
  
    await search_page.gotoSearchPage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Search Page', () => {
    test('shows expected sections', async ({ page }) => {
        const search_page = new SearchPage(page);

        await expect(search_page.mainMenu).toHaveScreenshot('search_page_mainMenu.png');
        await expect(search_page.searchBar).toHaveScreenshot('search_page_searchBar.png');
        await expect(search_page.footerSection).toHaveScreenshot('search_page_footerSection.png', { maxDiffPixelRatio: 0.01 });
    });
});
