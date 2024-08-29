import { base_page } from '../common/selectors.json';


export class BasePage {
  // Locators
  constructor(page) {
    this.page = page;
    
    this.mainMenu = page.locator(base_page.mainMenu);
    this.joinLoginButton = page.getByLabel(base_page.joinLoginButton);
    this.joinLoginDialog = page.locator(base_page.joinLoginDialog);
    this.loginLink = page.locator(base_page.loginLink);
    this.signupLink = page.locator(base_page.signupLink);
    this.closeButton = page.locator(base_page.closeButton);
    this.topBar = page.locator(base_page.topBar);
    this.brokerageSection = page.locator(base_page.brokerageSection);
    this.footerSection = page.locator(base_page.footerSection);
  }

  // Methods
  async showJoinLoginDialog() {
    await this.joinLoginButton.click();
  }

  async closeDialog() {
    await this.closeButton.click();
  }
}
