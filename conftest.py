import logging
import os

from pytest import fixture
from selenium import webdriver


@fixture(scope='session')
def initialized_browser():
    """
    Фикстура с настройка браузера для проведения теста
    :return:
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": f"{os.getcwd()}",
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "safebrowsing.disable_download_protection": True
    })

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.close()


def setup_logger():
    """
    Стандартные настройки логгера
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("tensor_autotests_log.log", mode='w'),
            logging.StreamHandler()
        ],
        force=True
    )


@fixture(scope='session')
def logger():
    """
    Проинициалированный логгер, который можно использовать в функциях программы
    """
    setup_logger()
    return logging.getLogger("Tensor-Autotests-Logger")
