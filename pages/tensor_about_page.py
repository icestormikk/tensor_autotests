from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

TENSOR_ABOUT_PAGE_URL = "https://tensor.ru/about"

we_are_working_images_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image')
we_are_working_images_container_selector = (By.CLASS_NAME, 'tensor_ru-About__block3')


class TensorAboutPage(BasePage):
    """
    Страница "О нас" сайта Тензор
    """

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def open(self):
        self.browser.get(TENSOR_ABOUT_PAGE_URL)

    @property
    def we_are_working_images(self) -> list[WebElement]:
        return self.find_many(we_are_working_images_selector)

    @property
    def we_are_working_images_container(self):
        return self.find(we_are_working_images_container_selector)
