import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import *
from locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, USERNAME).send_keys(CORRECT_LOGIN)
    driver.find_element(By.XPATH, PASSWORD).send_keys(CORRECT_PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()


@pytest.fixture
def cart_with_item(driver, login):
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.get(CHECKOUT_PAGE)
