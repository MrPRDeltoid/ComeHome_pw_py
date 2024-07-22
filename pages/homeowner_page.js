import { BasePage} from './base_page'
import { homeowner_page } from '../common/selectors.json';


exports.HomeownerPage = class HomeownerPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.mainSection = page.locator(homeowner_page.mainSection);
        this.avmSection = page.locator(homeowner_page.avmSection);
        this.cardsSection = page.locator(homeowner_page.cardsSection);
    }
    // Methods
    async gotoHomeownerPage() {
        await this.page.goto('/homeowner');
    }
}
