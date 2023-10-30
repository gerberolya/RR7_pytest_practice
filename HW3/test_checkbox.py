from selenium.webdriver.common.by import By


def test_checkbox_is_selected(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    first_checkbox = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
    second_checkbox = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
    first_checkbox.click()
    assert second_checkbox.is_selected()
    assert second_checkbox.is_selected()

def test_checkbox_place(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    place_cb1 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)').rect['x']
    place_cb2 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)').rect['x']
    assert place_cb1 == place_cb2 # элементы выравнены по оси х
