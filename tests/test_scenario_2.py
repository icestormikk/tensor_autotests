from pytest import mark
from selenium.webdriver.support import expected_conditions

from pages.sbis_contacts_page import SbisContactsPage, region_chooser_text_selector, YAR_OBL_LABEL, \
    KAMCHATKA_KRAI_LABEL, SBIS_CONTACTS_PAGE_URL


def partners_verify(page: SbisContactsPage):
    """
    Валидация списка партнёров (проверка на наличие списка и его не пустоту)
    :param page: Страница "Контакты" сайта Сбис
    :return: None
    """
    assert page.partners_list is not None
    assert len(page.partners) > 0


def region_chooser_real_region_verify(page: SbisContactsPage):
    """
    Валидация текста на кнопке выбора региона (соответствие реальному местоположению)
    :param page: Страница "Контакты" сайта Сбис
    :return: None
    """
    region_chooser_text = page.region_chooser_text
    assert region_chooser_text == YAR_OBL_LABEL


def region_chooser_is_exists(page: SbisContactsPage):
    """
    Проверка вызова модального окна при нажатии на кнопку смены региона
    :param page: Страница "Контакты" сайта Сбис
    :return: None
    """
    # находим кнопку для смены региона
    region_chooser = page.region_chooser
    # ждём, когда она станет кликабельной
    page.wait_until(expected_conditions.element_to_be_clickable(region_chooser))
    # нажимаем на неё
    region_chooser.click()

    # находим на странице модальное окно
    region_chooser_dialog = page.region_chooser_dialog
    # проверяем его наличие
    assert region_chooser_dialog is not None


def region_choose_dialog_verify(page: SbisContactsPage):
    """
    Проверка корректности работы механизма по смене региона
    :param page: Страница "Контакты" сайта Сбис
    :return: None
    """
    # ждём появляения поисковой строки в модальном окне, что будет означать, что окно полностью загрузилось
    page.wait_until(expected_conditions.visibility_of(page.region_chooser_dialog_searchbar))

    # находим на странице вариант "Камчатский край"
    kamchatka_krai_dialog_option = page.kamchatka_krai_dialog_option
    # ждём, пока он не станет кликабельным
    page.wait_until(expected_conditions.element_to_be_clickable(kamchatka_krai_dialog_option))
    # нажимаем на него
    kamchatka_krai_dialog_option.click()

    # ждём пока текст на кнопке смены региона не поменяется на другой (любой)
    page.wait_until_not(
        expected_conditions.text_to_be_present_in_element(region_chooser_text_selector, YAR_OBL_LABEL)
    )

    # получаем новый текст
    update_region_chooser_text = page.region_chooser_text

    assert KAMCHATKA_KRAI_LABEL in update_region_chooser_text
    assert KAMCHATKA_KRAI_LABEL in page.browser.title


@mark.scenario_2
def test_scenario_2(initialized_browser, logger):
    """
    Второй тестовый сценарий
    :param initialized_browser: Настроенный нужным образом браузер
    :return: None
    """
    logger.info(f"Открываем страницу {SBIS_CONTACTS_PAGE_URL}")
    sbis_contacts_page = SbisContactsPage(initialized_browser)
    sbis_contacts_page.open()

    logger.info(f"Проверяем, соответствует ли нашего текущее местоположение ({YAR_OBL_LABEL}) указанному в поле")
    region_chooser_real_region_verify(sbis_contacts_page)
    logger.info("Проверяем список партнёров")
    partners_verify(sbis_contacts_page)

    logger.info("Проверяем, открывается ли модальное окно со списком всех регионов")
    region_chooser_is_exists(sbis_contacts_page)
    logger.info("Проверяем функционал смены региона")
    region_choose_dialog_verify(sbis_contacts_page)
