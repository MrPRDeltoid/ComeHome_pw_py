import { test, expect } from '@playwright/test';
import { HomePage } from '../pages/home_page.js';


test.beforeEach('Load Home Page and launch dialog', async ({ page }) => {
    const home_page = new HomePage(page);
  
    await home_page.gotoHomePage();
    await home_page.showJoinLoginDialog();
});
  
test.afterEach('Close the dialog and browser', async ({ page }) => {
    const home_page = new HomePage(page);
    
    await home_page.closeDialog();
    await page.close();
});

test.describe('The Join/Login Dialog signup view', () => {
    test('shows expected elements', async ({ page }) => {
      const home_page = new HomePage(page);

      await expect(home_page.joinLoginDialog).toHaveScreenshot('home_page_joinLoginDialog_signup.png');
  });
});

test.describe('The Join/Login Dialog login view', () => {
    test('shows expected elements', async ({ page }) => {
        const home_page = new HomePage(page);

        await home_page.loginLink.click()
        await expect(home_page.joinLoginDialog).toHaveScreenshot('home_page_joinLoginDialog_login.png');
    });
});
