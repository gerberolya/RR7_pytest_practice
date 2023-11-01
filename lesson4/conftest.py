import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def options():
    options = Options()
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# @pytest.fixture(scope='class')
# def creds(request):
#     request.cls.login = 'jhgj@olm.hj'
#     request.cls.password = '7P@G@xcMYRezL5U'
#
# @pytest.fixture
# def cred():
#     login = 'jhgj@olm.hj'
#     password = '7P@G@xcMYRezL5U'
#     return login, password
