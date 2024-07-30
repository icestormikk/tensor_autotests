from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

TENSOR_ABOUT_PAGE_URL = "https://tensor.ru/about"

we_are_working_images_selector = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image')


def is_images_have_same_size(images: list[WebElement]) -> bool:
    if not images:
        return True

    width = images[0].size.get('width')
    height = images[0].size.get('height')

    for image in images:
        sizes_dict = image.size
        if sizes_dict.get('width') != width or sizes_dict.get('height') != height:
            return False

    return True


class TensorAboutPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def open(self):
        self.browser.get(TENSOR_ABOUT_PAGE_URL)

    @property
    def we_are_working_images(self) -> list[WebElement]:
        return self.find_many(we_are_working_images_selector)
