from selenium.webdriver.remote.webelement import WebElement
from lesson4.pages.basepage import BasePage
from lesson4.data.locators import SignInPageLocators
from lesson4.data.auth_data import CORRECT_LOGIN, CORRECT_PASSWORD



class SignInPage(BasePage):
    def email_field_is_present(self) -> WebElement:
        return self.is_visible(SignInPageLocators.EMAIL_FIELD)

    def pass_field_is_present(self) -> WebElement:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD)

    def sign_in_button_is_clickable(self) -> WebElement:
        return self.is_clickable(SignInPageLocators.SIGN_IN_BUTTON)

    def fill_in_the_form(self):
        self.email_field_is_present().send_keys(CORRECT_LOGIN)
        self.pass_field_is_present().send_keys(CORRECT_PASSWORD)
        self.sign_in_button_is_clickable().click()