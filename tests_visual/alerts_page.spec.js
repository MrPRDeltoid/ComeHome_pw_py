import { test, expect } from '@playwright/test';
import { AlertsPage } from '../pages/alerts_page.js';


test.beforeEach('Load Alerts Page', async ({ page }) => {
    const alerts_page = new AlertsPage(page);
  
    await alerts_page.gotoAlertsPage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Alerts Page', () => {
    test('has expected sections', async ({ page }) => {
        const alerts_page = new AlertsPage(page);

        await expect(alerts_page.mainMenu).toHaveScreenshot('alerts_page_mainMenu.png');
        await expect(alerts_page.headerSection).toHaveScreenshot('alerts_page_headerSection.png');
        await expect(alerts_page.loggedOutSection).toHaveScreenshot('alerts_page_loggedOutSection.png');
        await expect(alerts_page.footerSection).toHaveScreenshot('alerts_page_footerSection.png');
    });
});
