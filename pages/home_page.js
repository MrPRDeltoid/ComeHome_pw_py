import { expect, page } from '@playwright/test';
import { BasePage} from './base_page'
import { home_page } from '../common/selectors.json';


exports.HomePage = class HomePage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.topSection = page.locator(home_page.topSection);
        this.photoSection = page.locator(home_page.photoSection);
        this.trackOrBuySection = page.locator(home_page.trackOrBuySection);
        this.agentSection = page.locator(home_page.agentSection);
    }
    // Methods
    async gotoHomePage() {
        await this.page.goto('/');
    }
}
