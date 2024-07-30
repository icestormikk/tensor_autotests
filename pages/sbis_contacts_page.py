from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

SBIS_CONTACTS_PAGE_URL = "https://sbis.ru/contacts"
YAR_OBL_LABEL = "Ярославская обл."
KAMCHATKA_KRAI_LABEL = "Камчатский край"

region_chooser_selector = (
    By.CSS_SELECTOR, '.sbisru-Contacts .sbis_ru-Region-Chooser'
)
region_chooser_text_selector = (
    By.CSS_SELECTOR, '.sbisru-Contacts .sbis_ru-Region-Chooser__text'
)
region_chooser_dialog_selector = (
    By.XPATH, '//div[@name="dialog" and contains(@class, "sbis_ru-Region-Panel")]'
)
region_chooser_dialog_searchbar_selector = (
    By.CSS_SELECTOR, '.sbis_ru-Region-Panel__search'
)
kamchatka_krai_option_selector = (
    By.XPATH, '//ul[contains(@class, "sbis_ru-Region-Panel__list-l")]//span[contains(@title,"Камчатский край")]'
)
partners_list_selector = (
    By.CSS_SELECTOR, '.sbisru-Contacts-City__flex .sbisru-Contacts-List__col'
)
footer_container_selector = (
    By.CLASS_NAME, 'sbisru-Footer__container'
)
download_local_versions_link_selector = (
    By.XPATH, '//div[@class="sbisru-Footer__container"]//a[contains(text(),"Скачать локальные версии")]'
)


class SbisContactsPage(BasePage):
    """
    Страница "Контакты" сайта Сбис
    """

    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    def open(self):
        self.browser.get(SBIS_CONTACTS_PAGE_URL)

    @property
    def kamchatka_krai_dialog_option(self):
        return self.find(kamchatka_krai_option_selector)

    @property
    def partners_list(self) -> WebElement:
        return self.find(partners_list_selector)

    @property
    def partners(self) -> list[WebElement]:
        return self.partners_list.find_elements(By.CSS_SELECTOR, 'div[name="itemsContainer"] > div')

    @property
    def region_chooser(self) -> WebElement:
        return self.find(region_chooser_selector)

    @property
    def region_chooser_text(self) -> str:
        region_chooser = self.find(region_chooser_selector)
        return region_chooser.text

    @property
    def region_chooser_dialog(self) -> WebElement:
        return self.find(region_chooser_dialog_selector)

    @property
    def region_chooser_dialog_searchbar(self) -> WebElement:
        return self.find(region_chooser_dialog_searchbar_selector)

    @property
    def footer_container(self):
        return self.find(footer_container_selector)

    @property
    def download_local_versions_link(self) -> WebElement:
        return self.find(download_local_versions_link_selector)
