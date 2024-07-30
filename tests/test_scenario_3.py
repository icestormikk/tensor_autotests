import os
import time
from logging import Logger

from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions

from pages.sbis_contacts_page import SbisContactsPage, SBIS_CONTACTS_PAGE_URL
from pages.sbis_download_page import SbisDownloadPage, PLUGIN_FILESIZE_IN_MB, SBIS_DOWNLOAD_PAGE_URL


def verify_sbis_installer_file(filename: str):
    """
    Проверка скачанного файла на соответствие размерам (в МБ)
    :param filename: имя файла, который необходимо проверить
    :return: None
    """
    filesize_in_mb = os.path.getsize(filename) / (1024 * 1024)
    assert round(filesize_in_mb, 2) == PLUGIN_FILESIZE_IN_MB


def wait_while_file_download(directory_for_download_path: str = ".", timeout_in_sec: int = 20):
    """
    Ожидание завершения загрузки одного или нескольких файлов в определённой директории
    :param directory_for_download_path: Путь к директории, куда загружаются файлы
    :param timeout_in_sec: Максимальное время ожидания завершения загрузки (в сек)
    :return: None
    """
    end_time = time.time() + timeout_in_sec
    while time.time() < end_time:
        downloading_files = [file.endswith(".crdownload") for file in os.listdir(directory_for_download_path)]
        if any(downloading_files):
            time.sleep(1)
        else:
            return

    raise TimeoutError(f"Не удалось скачать файл за установленное время: {timeout_in_sec}с")


def click_on_footer_link(page: SbisContactsPage):
    """
    Осуществление клика на ссылку "Скачать локальные версии"
    :param page: Страница "Контакты" сайта Сбис
    :return: None
    """
    link = page.download_local_versions_link
    # ждём, когда нужная нам ссылка в "подвале" страницы станет кликабельной
    page.wait_until(expected_conditions.element_to_be_clickable(link))

    page.browser.execute_script("arguments[0].scrollIntoView();", link)
    # переходим по ссылке по готовности
    ActionChains(page.browser).move_to_element(link).click(link).perform()
    # ждём, когда url страницы поменяется
    page.wait_until(expected_conditions.url_changes(SBIS_CONTACTS_PAGE_URL))


def click_on_download_variant(page: SbisDownloadPage, logger: Logger):
    """
    Поиск ссылки на скачивание нужного веб-установщика и скачивание плагина
    :param page: Страница "Загрузки" сайта Сбис
    :return: None
    """

    download_items_container = page.items_container
    # ждём загрузки блока с возможными вариантами загрузки
    page.wait_until(expected_conditions.visibility_of(download_items_container))

    windows_item_download = page.windows_item_download
    # ждём, когда кнопка для скачивания веб-инсталлятора на windows станет доступна
    page.wait_until(expected_conditions.element_to_be_clickable(windows_item_download))
    # нажимаем на ссылку по готовности
    windows_item_download.click()

    logger.debug("Ожидаем начало скачивания файла (2с)")
    # ждём, когда начнётся процесс скачивания файла
    time.sleep(2)
    logger.debug("Ожидаем завершение скачивания (40с)")
    # ожидание завершения процесса скачивания файла
    wait_while_file_download(timeout_in_sec=40)


@mark.scenario_3
def test_scenario_3(initialized_browser, logger):
    """
    Третий тестовый сценарий
    :param initialized_browser: Настроенный нужным образом браузер
    :return: None
    """
    logger.info(f"Открываем страницу {SBIS_CONTACTS_PAGE_URL}")
    sbis_contacts_page = SbisContactsPage(initialized_browser)
    sbis_contacts_page.open()

    logger.info("Переходим в \"подвал\" страницы и находим нужную ссылку")
    click_on_footer_link(sbis_contacts_page)

    logger.info(f"Открываем страницу {SBIS_DOWNLOAD_PAGE_URL}")
    sbis_download_page = SbisDownloadPage(initialized_browser)
    logger.info("Выбираем вариант с веб-установщиком для Windows и нажимаем на него")
    click_on_download_variant(sbis_download_page, logger)

    logger.info("Проверяем размера скачанного файла..")
    verify_sbis_installer_file("sbisplugin-setup-web.exe")
