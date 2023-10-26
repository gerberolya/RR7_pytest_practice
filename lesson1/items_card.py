from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import choice


def test_open_items_card_by_image(driver, login):
    first_item_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

    item_image = driver.find_element(By.CSS_SELECTOR, 'img.inventory_item_img')
    item_image.click()

    product_card_item_name = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text

    assert first_item_name == product_card_item_name




def test_open_items_card_by_name(driver, login):
    all_items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    random_item = choice(all_items)
    item_name = random_item.text
    random_item.click()
    product_card_item_name = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text

    assert item_name == product_card_item_name


