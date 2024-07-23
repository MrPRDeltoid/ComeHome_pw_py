import { BasePage} from './base_page'
import { watchlist_page } from '../common/selectors.json';


exports.WatchlistPage = class WatchlistPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.headerSection = page.locator(watchlist_page.headerSection);
        this.loggedOutSection = page.locator(watchlist_page.loggedOutSection);
    }
    
    // Methods
    async gotoWatchlistPage() {
        await this.page.goto('/watchlist');
    }
}
