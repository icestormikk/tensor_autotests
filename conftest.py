from pytest import fixture
from selenium import webdriver


@fixture()
def initialized_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.close()
