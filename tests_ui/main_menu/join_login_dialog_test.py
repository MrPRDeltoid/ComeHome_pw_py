import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@pytest.fixture()
def launch_close_dialog(home_page: HomePage):
    home_page.showJoinLoginDialog()
    yield
    home_page.closeDialog()

def test_verify_dialog_items_signup(home_page: HomePage, setup, launch_close_dialog):
    """Verify contents and elements of the signup dialog"""
    expect(home_page.joinLoginDialog).to_be_visible()
    expect(home_page.title).to_have_text("Welcome")
    expect(home_page.subTitle).to_have_text("Please sign up for a ComeHome account.")
    expect(home_page.loginRow).to_have_text("Already have an account?\nLog in")
    expect(home_page.firstnameField).to_be_visible()
    expect(home_page.lastnameField).to_be_visible()
    expect(home_page.emailField).to_be_visible()
    expect(home_page.phoneField).to_be_visible()
    expect(home_page.passwordField).to_be_visible()
    expect(home_page.confirmRow).to_have_text("Terms of Service AgreementBy registering, I agree to ComeHome\nTerms of Use\nand\nPrivacy Policy")
    expect(home_page.signupButton).to_have_text("Sign Up")
    expect(home_page.signupButton).to_be_disabled()

def test_verify_dialog_items_login(home_page: HomePage, setup, launch_close_dialog):
    """Verify contents and elements of the login dialog"""
    expect(home_page.joinLoginDialog).to_be_visible()
    home_page.loginLink.click()
    expect(home_page.title).to_have_text("Welcome")
    expect(home_page.subTitle).to_have_text("Please log in to your account")
    expect(home_page.signupRow).to_have_text("Don't have an account?\nSign up")
    expect(home_page.firstnameField).to_be_hidden()
    expect(home_page.lastnameField).to_be_hidden()
    expect(home_page.emailField).to_be_visible()
    expect(home_page.phoneField).to_be_hidden()
    expect(home_page.passwordField).to_be_visible()
    expect(home_page.confirmRow).to_be_hidden()
    expect(home_page.loginButton).to_have_text("Log In")
    expect(home_page.loginButton).to_be_disabled()
