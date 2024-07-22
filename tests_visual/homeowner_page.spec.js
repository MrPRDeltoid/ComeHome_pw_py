import { test, expect } from '@playwright/test';
import { HomeownerPage } from '../pages/homeowner_page.js';


test.beforeEach('Load Homeowner Page', async ({ page }) => {
    const homeowner_page = new HomeownerPage(page);
  
    await homeowner_page.gotoHomeownerPage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
     await page.close();
  });

test.describe('The Homeowner Page when no property selected', () => {
    test('has expected sections', async ({ page }) => {
        const homeowner_page = new HomeownerPage(page);

        await expect(homeowner_page.mainMenu).toHaveScreenshot('homeowner_page_mainMenu.png');
        await expect(homeowner_page.mainSection).toHaveScreenshot('homeowner_page_mainSection.png');
        await expect(homeowner_page.footerSection).toHaveScreenshot('homeowner_page_footerSection.png');
    });
});
