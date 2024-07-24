import { BasePage} from './base_page'
import { property_page } from '../common/selectors.json';


exports.PropertyPage = class PropertyPage extends BasePage {
    // Locators
    constructor(page) {
        super(page);
        this.page = page;

        this.topBar = page.locator(property_page.topBar);
        this.photoSection = page.locator(property_page.photoSection);
        this.propertyOptionsPanel = page.locator(property_page.propertyOptionsPanel);
        this.propertyIntroSection = page.locator(property_page.propertyIntroSection);
        this.propertyDetailsSection = page.locator(property_page.propertyDetailsSection);
        this.claimHomeSection = page.locator(property_page.claimHomeSection);
        this.mapSection = page.locator(property_page.mapSection);
    }
    
    // Methods
    async gotoPropertyPage(slug) {
        await this.page.goto(`/property-details/${slug}`);
    }
}
