import { BasePage} from './base_page'
import { agent_page } from '../common/selectors.json';


exports.AgentPage = class AgentPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.topSection = page.locator(agent_page.topSection);
        this.subSection = page.locator(agent_page.subSection);
    }
    
    // Methods
    async gotoAgentPage() {
        await this.page.goto('/concierge-team');
    }
}
