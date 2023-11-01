import pytest

from lesson4.pages.main_page import MainPage
from lesson4.pages.sign_in_page import SignInPage
from lesson4.data.urls import URL_LUMA
from lesson4.conftest import *

#@pytest.mark.usefixtures('creds')
class TestSignIn:

    def test_sign_in_positive(self, driver):
        main_page = MainPage(driver, URL_LUMA)
        main_page.open()
        main_page.sign_in_link().click()
        #assert driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/login'
        sign_in_page = SignInPage(driver, driver.current_url)
        sign_in_page.fill_in_the_form()
        assert main_page.welcome_is_present()
