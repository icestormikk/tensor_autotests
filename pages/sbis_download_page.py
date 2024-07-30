from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

SBIS_DOWNLOAD_PAGE_URL = 'https://sbis.ru/download?tab=plugin&innerTab=default'
PLUGIN_FILESIZE_IN_MB = 11.05

items_container_selector = (
    By.CLASS_NAME, "sbis_ru-DownloadNew-innerTabs"
)
items_download_selector = (
    By.XPATH,
    '//*[contains(@class, "sbis_ru-DownloadNew-innerTabs")]//a[contains(@class, "sbis_ru-DownloadNew-loadLink__link")]'
)


class SbisDownloadPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def open(self):
        self.browser.get(SBIS_DOWNLOAD_PAGE_URL)

    @property
    def items_container(self) -> WebElement:
        return self.find(items_container_selector)

    @property
    def items_download(self) -> list[WebElement]:
        return self.find_many(items_download_selector)

    @property
    def windows_item_download(self):
        return self.items_download[0]
