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
    expect(home_page.loginButton).to_have_text("Log In")
    expect(home_page.loginButton).to_be_disabled()

def test_missing_required_fields_signup(home_page: HomePage, setup, launch_close_dialog):
    """Tab through all fields, verifying correct error message appears for required fields"""
    home_page.firstnameField.press('Tab')
    home_page.lastnameField.press('Tab')
    home_page.emailField.press('Tab')
    home_page.phoneField.press('Tab')
    home_page.passwordField.press('Tab')
    exp_errors = ['Please enter your first name', 'Please enter your last name', 'Please enter your email', 'Please enter your password']
    expect(home_page.errorMessage).to_have_count(len(exp_errors))
    for error in range(len(exp_errors)):
        expect(home_page.errorMessage.nth(error)).to_have_text(exp_errors[error])
    expect(home_page.signupButton).to_be_disabled()

def test_invalid_email_valid_password_signup(home_page: HomePage, setup, launch_close_dialog):
    """Enter valid required info and invalid email to verify correct error message and button activation in Signup view"""
    home_page.fillSignupDialogFields(first_name='First', last_name='Last', password='Password123')
    home_page.emailField.fill('invalid_email')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Invalid email')
    home_page.signupButton.click()
    expect(home_page.errorMessage).to_have_text('the given email is unsupported')
    home_page.emailField.fill('invalid_email@gmail')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Invalid email')
    home_page.signupButton.click()
    expect(home_page.errorMessage).to_have_text('the given email is unsupported')
    home_page.emailField.fill('valid_email@gmail.com')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(0)
    expect(home_page.signupButton).to_be_enabled()

def test_valid_email_invalid_password_signup(home_page: HomePage, setup, launch_close_dialog):
    """Enter valid required info and invalid password to verify correct error message and button activation in Signup view"""
    home_page.fillSignupDialogFields(first_name='First', last_name='Last', email='valid_email@gmail.com')
    home_page.passwordField.fill('1234')
    home_page.passwordField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Password must be at least 8 characters')
    home_page.signupButton.click()
    expect(home_page.errorMessage).to_have_text('password must be 8 or more characters and cannot be a common dictionary word')
    home_page.passwordField.fill('12345678')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(0)
    expect(home_page.signupButton).to_be_enabled()

def test_invalid_email_valid_password_login(home_page: HomePage, setup, launch_close_dialog):
    """Enter valid password and invalid email to verify correct error message and button activation in Login view"""
    home_page.loginLink.click()
    home_page.fillLoginDialogFields(password='Password123')
    home_page.emailField.fill('invalid_email')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Invalid email')
    expect(home_page.loginButton).to_be_disabled()
    home_page.emailField.fill('invalid_email@gmail')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Invalid email')
    expect(home_page.loginButton).to_be_disabled()
    home_page.emailField.fill('valid_email@gmail.com')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(0)
    expect(home_page.loginButton).to_be_enabled()

def test_valid_email_invalid_password_login(home_page: HomePage, setup, launch_close_dialog):
    """Enter valid email and invalid password to verify correct error message and button activation in Login view"""
    home_page.loginLink.click()
    home_page.fillLoginDialogFields(email='valid_email@gmail.com')
    home_page.passwordField.fill('1234')
    home_page.passwordField.press('Tab')
    expect(home_page.errorMessage).to_have_count(1)
    expect(home_page.errorMessage).to_have_text('Password must be at least 8 characters')
    expect(home_page.loginButton).to_be_disabled()
    home_page.passwordField.fill('12345678')
    home_page.emailField.press('Tab')
    expect(home_page.errorMessage).to_have_count(0)
    expect(home_page.signupButton).to_be_enabled()
