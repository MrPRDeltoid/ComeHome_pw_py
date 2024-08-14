import json
from pathlib import Path
from playwright.sync_api import Page


class BasePage:
    """Locators and methods common to all pages"""
    BASE_URL = 'https://www.comehome.com/'
    SELECTORS_FILE_PATH = Path("common/selectors.json")

    # Locators
    def __init__(self, page: Page):
        self.page = page

        # Load in common selectors from json file
        with open(self.SELECTORS_FILE_PATH, mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['base_page']

        # Main Menu
        self.mainMenu = page.locator(selectors['mainMenu'])
        self.logo = self.mainMenu.locator('[data-hc-name=comehome-logo]')
        self.buyHomeButton = self.mainMenu.locator('[data-hc-name=buy-home-button]')
        self.myHomeButton = self.mainMenu.locator('[data-hc-name=my-home-button]')
        self.savedButton = self.mainMenu.locator('[data-hc-name=saved-button]')
        self.alertsButton = self.mainMenu.locator('[data-hc-name=alerts-button]')
        self.findAnAgentButton = self.mainMenu.locator('[data-hc-name=find-an-agent-button]')
        self.joinLoginButton = self.mainMenu.get_by_label(selectors['joinLoginButton'])
        # Brokerage Attribution Section
        self.brokerageSection = self.page.locator('[class$=__BrokerageAttribution]')
        self.brokerageLogo = self.brokerageSection.locator(self.logo)
        self.brokerageContactLink = self.brokerageSection.locator('.BrokerageAttribution__Link')
        self.brokerageText = self.brokerageSection.locator('.BrokerageAttribution__BrokerageSection')
        # Join Login Dialog
        self.joinLoginDialog = page.locator(selectors['joinLoginDialog'])
        self.dialogHeader = self.joinLoginDialog.locator('[data-hc-name=modal-header]')
        self.closeButton = self.joinLoginDialog.locator(selectors['closeButton'])
        self.title = self.joinLoginDialog.locator('.AuthModal__Title')
        self.subTitle = self.joinLoginDialog.locator('.AuthModal__Subtitle')
        self.loginRow = self.joinLoginDialog.locator('[data-hc-name=log-in-row]')
        self.loginLink = self.joinLoginDialog.locator(selectors['loginLink'])
        self.signupRow = self.joinLoginDialog.locator('[data-hc-name=sign-up-row]')
        self.signupLink = self.joinLoginDialog.locator(selectors['signupLink'])
        self.firstnameField = self.joinLoginDialog.get_by_label('first name')
        self.lastnameField = self.joinLoginDialog.get_by_label('last name')
        self.emailField = self.joinLoginDialog.get_by_label('email')
        self.phoneField = self.joinLoginDialog.get_by_label('phone')
        self.passwordField = self.joinLoginDialog.locator('[name=password]')
        self.confirmRow = self.joinLoginDialog.locator('[data-hc-name=confirm-row]')
        self.confirmCheck = self.confirmRow.get_by_role('checkbox')
        self.signupButton = self.joinLoginDialog.get_by_role('button', name = "Sign Up")
        self.loginButton = self.joinLoginDialog.get_by_role('button', name="Log In")
        self.errorMessage = self.joinLoginDialog.get_by_role('alert')
        # Top Bar Section common to Property Page and Homeowner Page
        self.topBar = page.locator(selectors['topBar'])
        self.breadcrumbs = self.topBar.locator('[data-hc-name=breadcrumbs]')
        self.publicViewButton = self.topBar.locator('[data-hc-name=public-view-button]')
        self.ownerViewButton = self.topBar.locator('[data-hc-name=owner-view-button]')
        # Footer Section
        self.footerSection = page.locator(selectors['footerSection'])

    # Methods
    def showJoinLoginDialog(self):
        self.joinLoginButton.click()
    
    def fillJoinLoginDialogFields(self, first_name='', last_name='', email='', phone='', password='', check=True):
        if self.subTitle.text_content() == "Please sign up for a ComeHome account.":  # The Signup view is shown with additional fields
            self.firstnameField.fill(first_name)
            self.lastnameField.fill(last_name)
            self.phoneField.fill(phone)
            if check:
                self.confirmCheck.check()
        self.emailField.fill(email)
        self.passwordField.fill(password)
    
    def get_property_data(self, property):
        with open(r".\.\data\properties.json", mode="r", encoding="utf-8") as data_file:
            property_data = json.load(data_file)[property]
        return property_data
    
    def construct_full_address(self, data):
        full_address = f"{data['street']} {data['city']} {data['state']} {data['zip']}"
        return full_address
    
    def construct_slug(self, data):
        full_address = self.construct_full_address(data)
        slug = f"{full_address}".replace(' ', '-')
        return slug

    def closeDialog(self):
        self.closeButton.click()
