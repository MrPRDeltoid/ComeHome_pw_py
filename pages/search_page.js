import { BasePage} from './base_page'
import { search_page } from '../common/selectors.json';


exports.SearchPage = class SearchPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.searchBar = page.locator(search_page.searchBar);
        this.moreFiltersButton = page.locator(search_page.moreFiltersButton)
        this.moreFiltersMenu = page.locator(search_page.moreFiltersMenu)
        this.mapSection = page.locator(search_page.mapSection);
        this.propertySection = page.locator(search_page.propertySection);
    }
    
    // Methods
    async gotoSearchPage() {
        await this.page.goto('/search');
    }
}
