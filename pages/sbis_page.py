from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

contacts_button_selector = (By.CSS_SELECTOR, ".sbisru-Header a[href='/contacts']")
tensor_image_selector = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')

SBIS_PAGE_URL = "https://sbis.ru/"


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(SBIS_PAGE_URL)

    @property
    def header_contacts_link(self):
        return self.find(contacts_button_selector)

    @property
    def tensor_image(self):
        return self.find(tensor_image_selector)

    def click_contacts(self):
        contacts_link = self.header_contacts_link
        ActionChains(self.browser).click(contacts_link).perform()

    def click_on_tensor_image(self):
        image = self.tensor_image
        ActionChains(self.browser).click(image).perform()
