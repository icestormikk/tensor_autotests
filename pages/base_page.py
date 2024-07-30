from abc import ABC, abstractmethod

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(ABC):
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, element_selector: tuple[str, str], timeout: int = 10) -> WebElement | None:
        try:
            return WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located(element_selector)
            )
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None

    def find_many(self, elements_selector: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_all_elements_located(elements_selector)
            )
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None

    def wait_until(self, condition, timeout: int = 20):
        WebDriverWait(self.browser, timeout).until(condition)

    def wait_until_not(self, condition, timeout: int = 20):
        WebDriverWait(self.browser, timeout).until_not(condition)

    @abstractmethod
    def open(self):
        pass
