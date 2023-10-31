import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from lesson1.locators.product_page_locators import FILTER


def test_filter_a_to_z(driver, login):
    select = Select(driver.find_element(By.XPATH, FILTER))

    # select by visible text
    select.select_by_visible_text('Name (A to Z)')
    all_items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    all_names = []
    for i in all_items:
        all_names.append(i.text)
    assert all_names == sorted(all_names)


def test_filter_z_to_a(driver, login):
    select = Select(driver.find_element(By.XPATH, FILTER))

    # select by visible text
    select.select_by_visible_text('Name (Z to A)')
    all_items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    all_names = []
    for i in all_items:
        all_names.append(i.text)
    assert all_names == sorted(all_names)[::-1]


def test_filter_low_to_high(driver, login):
    select = Select(driver.find_element(By.XPATH, FILTER))

    # select by visible text
    select.select_by_visible_text('Price (low to high)')
    all_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    list_of_prices = []
    for i in all_prices:
        list_of_prices.append(float(i.text[1:]))
    assert list_of_prices == sorted(list_of_prices)


def test_filter_high_to_low(driver, login):
    select = Select(driver.find_element(By.XPATH, FILTER))

    # select by visible text
    select.select_by_visible_text('Price (high to low)')
    all_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    list_of_prices = []
    for i in all_prices:
        list_of_prices.append(float(i.text[1:]))
    assert list_of_prices == sorted(list_of_prices)[::-1]
