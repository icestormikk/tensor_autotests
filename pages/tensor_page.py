from selenium.webdriver.common.by import By

from pages.base_page import BasePage

TENSOR_SITE_URL = "https://tensor.ru/"
TENSOR_ABOUT_PAGE_URL = "https://tensor.ru/about"

power_in_people_text_selector = (By.XPATH, '//*[text()="Сила в людях"]')
power_in_people_more_button_selector = (By.XPATH, '//*[text()="Сила в людях"]/following-sibling::p//a')

tensor_page_indicator_selector = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(TENSOR_SITE_URL)

    @property
    def power_in_people_text(self):
        return self.find(*power_in_people_text_selector)

    @property
    def power_in_people_more_button(self):
        return self.find(*power_in_people_more_button_selector)

    def click_on_power_in_people_more_button(self):
        button = self.power_in_people_more_button
        self.browser.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

