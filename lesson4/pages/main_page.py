from selenium.webdriver.remote.webelement import WebElement
from lesson4.pages.basepage import BasePage
from lesson4.data.locators import MainPageLocators


class MainPage(BasePage):
    def sign_in_link(self) -> WebElement:
        return self.is_clickable(MainPageLocators.SIGN_IN_LINK)

    def welcome_is_present(self) -> WebElement:
        return self.is_visible(MainPageLocators.WELCOME)


