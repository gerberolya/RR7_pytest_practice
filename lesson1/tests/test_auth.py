import time

from selenium.webdriver.common.by import By

from lesson1.data.auth_data import PRODUCT_LIST, CORRECT_LOGIN, CORRECT_PASSWORD, INCORRECT_LOGIN, INCORRECT_PASSWORD
from lesson1.locators.main_page_locators import USERNAME, PASSWORD, LOGIN_BUTTON
from data import *


def test_login_form_correct(driver):

    driver.find_element(By.XPATH, USERNAME).send_keys(CORRECT_LOGIN)
    driver.find_element(By.XPATH, PASSWORD).send_keys(CORRECT_PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.current_url == PRODUCT_LIST

def test_login_form_uncorrect(driver):

    driver.find_element(By.XPATH, USERNAME).send_keys(INCORRECT_LOGIN)
    driver.find_element(By.XPATH, PASSWORD).send_keys(INCORRECT_PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    error_button_text = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text

    assert error_button_text == 'Epic sadface: Username and password do not match any user in this service'










