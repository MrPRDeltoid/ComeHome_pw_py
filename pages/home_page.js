import { expect, page } from '@playwright/test';
import { BasePage} from './base_page'


exports.HomePage = class HomePage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.topSection = page.locator('[class$="__TopSection"]');
        this.photoSection = page.locator('[class$="__PhotoSection"]');
        this.trackOrBuySection = page.locator('[class$="__HomeSubpageTrackOrBuyHome"]');
        this.agentSection = page.locator('[class$="__HomeSubpageYourTeamAgent"]');
    }
    // Methods
    async gotoHomePage() {
        await this.page.goto('/');
    }
}
