import { test, expect } from '@playwright/test';
import { PropertyPage } from '../pages/property_page.js';


test.beforeEach('Load Property Page', async ({ page }) => {
    const property_page = new PropertyPage(page);

    const slug = '199-El-Nido-Ave-Pasadena-CA-91107';
    await property_page.gotoPropertyPage(slug);
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Property Page', () => {
    test('shows expected sections', async ({ page }) => {
        const property_page = new PropertyPage(page);

        await expect(property_page.mainMenu).toHaveScreenshot('property_page_mainMenu.png');
        await expect(property_page.topBar).toHaveScreenshot('property_page_topBar.png');
        await expect(property_page.photoSection).toHaveScreenshot('property_page_photoSection.png');
        await expect(property_page.propertyOptionsPanel).toHaveScreenshot('property_page_propertyOptionsPanel.png', { maxDiffPixelRatio: 0.01 });
        await expect(property_page.propertyIntroSection).toHaveScreenshot('property_page_propertyIntroSection.png');
        await expect(property_page.propertyDetailsSection).toHaveScreenshot('property_page_propertyDetailsSection.png', { maxDiffPixelRatio: 0.01 });
        await expect(property_page.claimHomeSection).toHaveScreenshot('property_page_claimHomeSection.png');
        await expect(property_page.mapSection).toHaveScreenshot('property_page_mapSection.png');
        await expect(property_page.footerSection).toHaveScreenshot('property_page_footerSection.png');
    });
});
