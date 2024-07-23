import { BasePage} from './base_page'
import { alerts_page } from '../common/selectors.json';


exports.AlertsPage = class AlertsPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.headerSection = page.locator(alerts_page.headerSection);
        this.loggedOutSection = page.locator(alerts_page.loggedOutSection);
    }
    
    // Methods
    async gotoAlertsPage() {
        await this.page.goto('/alerts');
    }
}
