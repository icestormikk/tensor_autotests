from abc import ABC, abstractmethod

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(ABC):
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, *args) -> WebElement | None:
        try:
            return self.browser.find_element(*args)
        except NoSuchElementException:
            return None

    def find_many(self, *args):
        return self.browser.find_elements(*args)

    @abstractmethod
    def open(self):
        pass
