from playwright.sync_api import Page


class BasePage:
    """Locators and methods common to all pages"""
    BASE_URL = 'https://www.comehome.com/'

    # Locators
    def __init__(self, page: Page):
        self.page = page

        # Main Menu
        self.mainMenu = page.locator('[data-hc-name="top-section"]')
        self.logo = self.mainMenu.locator('[data-hc-name="comehome-logo"]')
        self.buyHomeButton = self.mainMenu.locator('[data-hc-name="buy-home-button"]')
        self.myHomeButton = self.mainMenu.locator('[data-hc-name="my-home-button"]')
        self.savedButton = self.mainMenu.locator('[data-hc-name="saved-button"]')
        self.alertsButton = self.mainMenu.locator('[data-hc-name="alerts-button"]')
        self.findAnAgentButton = self.mainMenu.locator('[data-hc-name="find-an-agent-button"]')
        self.joinLoginLink = self.mainMenu.get_by_label('Join or log in')
        # Join Login Dialog
        self.joinLoginDialog = page.locator('[class$="SlideInModal__ModalWithCloseIcon"]')
        self.dialogHeader = self.joinLoginDialog.locator('[data-hc-name="modal-header"]')
        self.closeButton = self.joinLoginDialog.locator('[data-hc-name="close-dialog-button"]')
        self.title = self.joinLoginDialog.locator('.AuthModal__Title')
        self.subTitle = self.joinLoginDialog.locator('.AuthModal__Subtitle')
        self.loginRow = self.joinLoginDialog.locator('[data-hc-name="log-in-row"]')
        self.loginLink = self.joinLoginDialog.locator('[data-event-name="click_login_cta"]')
        self.signupRow = self.joinLoginDialog.locator('[data-hc-name="sign-up-row"]')
        self.signupLink = self.joinLoginDialog.locator('[data-event-name="click_signup_cta"]')
        self.firstnameField = self.joinLoginDialog.get_by_label('first name')
        self.lastnameField = self.joinLoginDialog.get_by_label('last name')
        self.emailField = self.joinLoginDialog.get_by_label('email')
        self.phoneField = self.joinLoginDialog.get_by_label('phone')
        self.passwordField = self.joinLoginDialog.locator('[name="password"]')
        self.confirmRow = self.joinLoginDialog.locator('[data-hc-name="confirm-row"]')
        self.signupButton = self.joinLoginDialog.get_by_role('button', name = "Sign Up")
        self.loginButton = self.joinLoginDialog.get_by_role('button', name="Log In")
        # Footer Section
        self.footerSection = page.locator('[data-hc-name="footer-section"]')

    # Methods
    def showJoinLoginDialog(self):
        self.joinLoginLink.click()
    
    def closeDialog(self):
        self.closeButton.click()
