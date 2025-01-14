import { test, expect } from '@playwright/test';
import { SearchPage } from '../pages/search_page.js';


test.beforeEach('Load Search Page', async ({ page }) => {
    const search_page = new SearchPage(page);
  
    await search_page.gotoSearchPage();
  });
  
test.afterEach('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Search Page', () => {
    test('shows expected sections', async ({ page }) => {
        const search_page = new SearchPage(page);

        await expect(search_page.mainMenu).toHaveScreenshot('search_page_mainMenu.png');
        await expect(search_page.searchBar).toHaveScreenshot('search_page_searchBar.png');
        await expect(search_page.footerSection).toBeVisible()
        await expect(search_page.footerSection).toHaveScreenshot('search_page_footerSection.png', { maxDiffPixelRatio: 0.01 });
    });

    test('clicking More Filters shows correct menu', async ({ page }) => {
        const search_page = new SearchPage(page);

        await search_page.moreFiltersButton.click();
        await expect(search_page.moreFiltersMenu).toHaveScreenshot('search_page_moreFiltersMenu.png');
    });

    test('map section shows correct layer control panels', async ({ page }) => {
        const search_page = new SearchPage(page);

        await search_page.layerButtons.getByText("Crime").click();
        await expect(search_page.layerControlPanel).toHaveScreenshot('search_page_crimeLayerControlPanel.png', { maxDiffPixelRatio: 0.02 });
        await search_page.layerButtons.getByText("Schools").click();
        await expect(search_page.layerControlPanel).toHaveScreenshot('search_page_schoolsLayerControlPanel.png', { maxDiffPixelRatio: 0.02 });
        await search_page.layerButtons.getByText("Price").click();
        await expect(search_page.layerControlPanel).toHaveScreenshot('search_page_priceLayerControlPanel.png', { maxDiffPixelRatio: 0.02 });
        await search_page.layerButtons.getByText("Forecast").click();
        await expect(search_page.layerControlPanel).toHaveScreenshot('search_page_forecastLayerControlPanel.png', { maxDiffPixelRatio: 0.02 });
    });

    test('properties section shows correct brokerage info', async ({ page }) => {
        const search_page = new SearchPage(page);
        
        await expect(search_page.brokerageSection.last()).toBeVisible();
        await expect(search_page.brokerageSection.last()).toHaveScreenshot('search_page_brokerageSection.png');
    });
});
