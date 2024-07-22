import { expect } from '@playwright/test';
import { base_page } from '../common/selectors.json';


export class BasePage {
    constructor(page) {
        this.page = page;

        this.mainMenu = page.locator(base_page.mainMenu);
        this.joinLoginDialog = page.locator(base_page.joinLoginDialog);
        this.footerSection = page.locator(base_page.footerSection);
  }
}
