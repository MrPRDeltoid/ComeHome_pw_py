import { test, expect } from '@playwright/test';
import { HomePage } from '../pages/home_page.js';


test.beforeEach('Load Home Page', async ({ page }) => {
    const home_page = new HomePage(page);
  
    await home_page.gotoHomePage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Home Page', () => {
  test('has expected sections', async ({ page }) => {
      const home_page = new HomePage(page);

      await expect(home_page.mainMenu).toHaveScreenshot('home_page_mainMenu.png');
      await expect(home_page.topSection).toHaveScreenshot('home_page_topSection.png');
      await expect(home_page.photoSection).toHaveScreenshot('home_page_photoSection.png');
      await expect(home_page.trackOrBuySection).toHaveScreenshot('home_page_trackOrBuySection.png');
      await expect(home_page.agentSection).toHaveScreenshot('home_page_agentSection.png');
      await expect(home_page.footerSection).toHaveScreenshot('home_page_footerSection.png');
  });
});
