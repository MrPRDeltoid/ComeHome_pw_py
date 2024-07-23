import json
from playwright.sync_api import Page


class BasePage:
    """Locators and methods common to all pages"""
    BASE_URL = 'https://www.comehome.com/'

    # Locators
    def __init__(self, page: Page):
        self.page = page

        # Load in common selectors from json file
        with open(r".\common\selectors.json", mode="r", encoding="utf-8") as json_data:
            selectors = json.load(json_data)['base_page']

        # Main Menu
        self.mainMenu = page.locator(selectors['mainMenu'])
        self.logo = self.mainMenu.locator('[data-hc-name="comehome-logo"]')
        self.buyHomeButton = self.mainMenu.locator('[data-hc-name="buy-home-button"]')
        self.myHomeButton = self.mainMenu.locator('[data-hc-name="my-home-button"]')
        self.savedButton = self.mainMenu.locator('[data-hc-name="saved-button"]')
        self.alertsButton = self.mainMenu.locator('[data-hc-name="alerts-button"]')
        self.findAnAgentButton = self.mainMenu.locator('[data-hc-name="find-an-agent-button"]')
        self.joinLoginButton = self.mainMenu.get_by_label(selectors['joinLoginButton'])
        # Brokerage Attribution Section
        self.brokerageSection = self.page.locator('[class$="__BrokerageAttribution"]')
        self.brokerageLogo = self.brokerageSection.locator(self.logo)
        self.brokerageContactLink = self.brokerageSection.locator('.BrokerageAttribution__Link')
        self.brokerageText = self.brokerageSection.locator('.BrokerageAttribution__BrokerageSection')
        # Join Login Dialog
        self.joinLoginDialog = page.locator(selectors['joinLoginDialog'])
        self.dialogHeader = self.joinLoginDialog.locator('[data-hc-name="modal-header"]')
        self.closeButton = self.joinLoginDialog.locator(selectors['closeButton'])
        self.title = self.joinLoginDialog.locator('.AuthModal__Title')
        self.subTitle = self.joinLoginDialog.locator('.AuthModal__Subtitle')
        self.loginRow = self.joinLoginDialog.locator('[data-hc-name="log-in-row"]')
        self.loginLink = self.joinLoginDialog.locator(selectors['loginLink'])
        self.signupRow = self.joinLoginDialog.locator('[data-hc-name="sign-up-row"]')
        self.signupLink = self.joinLoginDialog.locator(selectors['signupLink'])
        self.firstnameField = self.joinLoginDialog.get_by_label('first name')
        self.lastnameField = self.joinLoginDialog.get_by_label('last name')
        self.emailField = self.joinLoginDialog.get_by_label('email')
        self.phoneField = self.joinLoginDialog.get_by_label('phone')
        self.passwordField = self.joinLoginDialog.locator('[name="password"]')
        self.confirmRow = self.joinLoginDialog.locator('[data-hc-name="confirm-row"]')
        self.signupButton = self.joinLoginDialog.get_by_role('button', name = "Sign Up")
        self.loginButton = self.joinLoginDialog.get_by_role('button', name="Log In")
        # Footer Section
        self.footerSection = page.locator(selectors['footerSection'])

    # Methods
    def showJoinLoginDialog(self):
        self.joinLoginButton.click()
    
    def closeDialog(self):
        self.closeButton.click()
