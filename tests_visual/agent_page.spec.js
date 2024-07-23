import { test, expect } from '@playwright/test';
import { AgentPage } from '../pages/agent_page.js';


test.beforeEach('Load Agent Page', async ({ page }) => {
    const agent_page = new AgentPage(page);
  
    await agent_page.gotoAgentPage();
  });
  
test.afterAll('Close the browser', async ({ page }) => {
    await page.close();
});

test.describe('The Agent Page', () => {
    test('shows expected sections', async ({ page }) => {
        const agent_page = new AgentPage(page);

        await expect(agent_page.mainMenu).toHaveScreenshot('agent_page_mainMenu.png');
        await expect(agent_page.topSection).toHaveScreenshot('agent_page_topSection.png');
        await expect(agent_page.subSection).toHaveScreenshot('agent_page_subSection.png');
        await expect(agent_page.footerSection).toHaveScreenshot('agent_page_footerSection.png');
    });
});
