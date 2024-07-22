import { BasePage} from './base_page'
import { search_page } from '../common/selectors.json';


exports.SearchPage = class SearchPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.searchBar = page.locator(search_page.searchBar);
        this.mapSection = page.locator(search_page.mapSection);
        this.propertySection = page.locator(search_page.propertySection);
    }
    // Methods
    async gotoSearchPage() {
        await this.page.goto('/search');
    }
}
