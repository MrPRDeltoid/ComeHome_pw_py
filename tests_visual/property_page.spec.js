import { test, expect } from '@playwright/test';
import { PropertyPage } from '../pages/property_page.js';


test.beforeEach('Load Property Page', async ({ page }) => {
    const property_page = new PropertyPage(page);

    const slug = '199-El-Nido-Ave-Pasadena-CA-91107';
    await property_page.gotoPropertyPage(slug);
  });
  
test.afterEach('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Property Page', () => {
    test('shows expected sections', async ({ page, browserName }) => {
        const property_page = new PropertyPage(page);

        await expect(property_page.mainMenu).toHaveScreenshot('property_page_mainMenu.png');
        await expect(property_page.topBar).toHaveScreenshot('property_page_topBar.png');
        if (browserName != 'firefox') {  // TODO: Image does not render in firefox before screenshot is taken
            await expect(property_page.photoSectionImage).toBeVisible();  // NOTE: Required to allow image to render
            await expect(property_page.photoSection).toHaveScreenshot('property_page_photoSection.png',
                { mask: [property_page.propertyOptionsPanel] });  // Mask out the overlaid options panel
        }
        await expect(property_page.propertyOptionsPanel).toHaveScreenshot('property_page_propertyOptionsPanel.png',
            { maxDiffPixelRatio: 0.01, mask: [property_page.propertyOptionsPanel.locator('[data-hc-name="listing-status"]')] }); // Mask out the listing status section, as values can change
        await expect(property_page.propertyIntroSection).toHaveScreenshot('property_page_propertyIntroSection.png');
        await expect(property_page.propertyDetailsSection).toHaveScreenshot('property_page_propertyDetailsSection.png',
            { maxDiffPixelRatio: 0.01 });  // NOTE: May need to be updated every year when Tax Year and Tax Amount may change
        await expect(property_page.claimHomeSection).toHaveScreenshot('property_page_claimHomeSection.png');
        await expect(property_page.mapSectionImage).toHaveAttribute('data-state', 'active');  // NOTE: Required to allow map to render
        if (browserName != 'firefox') {  // TODO: Investigate why firefox has issues with this image not loading succinctly
            await expect(property_page.mapSectionInfoButton).toBeVisible();  // NOTE: Required to allow image to render
            await expect(property_page.mapSection).toHaveScreenshot('property_page_mapSection.png');
        }   
        await expect(property_page.footerSection).toHaveScreenshot('property_page_footerSection.png',
            { maxDiffPixelRatio: 0.01 });
    });
});
