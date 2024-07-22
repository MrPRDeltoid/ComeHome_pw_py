import { expect } from '@playwright/test';


export class BasePage {
    constructor(page) {
        this.page = page;

        this.mainMenu = page.locator('[data-hc-name="top-section"]');
        this.joinLoginDialog = page.locator('[class$="SlideInModal__ModalWithCloseIcon"]');
        this.footerSection = page.locator('[data-hc-name="footer-section"]');
  }
}
