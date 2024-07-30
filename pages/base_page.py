from abc import ABC, abstractmethod

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(ABC):
    """
    Базовый класс для всех страниц приложения
    """

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, element_selector: tuple[str, str], timeout: int = 10) -> WebElement | None:
        """
        Поиск элемента на странице
        :param element_selector: селектор, с помощью которого можно найти элемент на странице
        :param timeout: Максимальное время поиска элемента
        :return: Элемент страницы в случае успешного поиска, иначе None
        """
        try:
            return WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located(element_selector)
            )
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None

    def find_many(self, elements_selector: tuple[str, str], timeout: int = 10):
        """
        Поиск нескольких элементов на странице
        :param elements_selector: селектор, с помощью которого можно найти элементы на странице
        :param timeout: Максимальное время поиска элементов
        :return: Элементы страницы в случае успешного поиска, иначе None
        """
        try:
            return WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_all_elements_located(elements_selector)
            )
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None

    def wait_until(self, condition, timeout: int = 20):
        """
        Ожидание успешного выполнения некоторого условия
        :param condition: условие, которое должно быть истинным
        :param timeout: Максимальное время ожидания выполнения условия
        :return: None
        """
        WebDriverWait(self.browser, timeout).until(condition)

    def wait_until_not(self, condition, timeout: int = 20):
        """
        Ожидание момента, когда условие будет ложно
        :param condition: условие, которое должно не выполняться
        :param timeout: Максимальное время ожидания
        :return: None
        """
        WebDriverWait(self.browser, timeout).until_not(condition)

    @abstractmethod
    def open(self):
        """
        Открытие страницы в браузере
        :return:
        """
        pass
