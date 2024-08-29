import { BasePage} from './base_page'
import { search_page } from '../common/selectors.json';


exports.SearchPage = class SearchPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.searchBar = page.locator(search_page.searchBar);
        this.moreFiltersButton = page.locator(search_page.moreFiltersButton);
        this.moreFiltersMenu = page.locator(search_page.moreFiltersMenu);
        this.mapSection = page.locator(search_page.mapSection);
        this.layerButtons = this.mapSection.getByRole('tablist').getByRole('tab');
        this.layerControlPanel = this.mapSection.locator(search_page.layerControlPanel);
        this.propertySection = page.locator(search_page.propertySection);
        this.lenderCard = page.locator(search_page.lenderCard);
    }
    
    // Methods
    async gotoSearchPage() {
        await this.page.goto('/search');
    }
}
