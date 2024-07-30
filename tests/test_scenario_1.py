from logging import Logger

from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from conftest import logger
from pages.sbis_page import SbisPage, SBIS_PAGE_URL
from pages.tensor_about_page import TensorAboutPage, TENSOR_ABOUT_PAGE_URL
from pages.tensor_page import TensorPage, POWER_IN_PEOPLE_LABEL, TENSOR_SITE_URL


def verify_we_are_working_images(page: TensorAboutPage, logger: Logger):
    """
    Валидация изображений в блоке "Работаем"
    :param page: Страница "О нас" сайта Тензор
    :return: None
    """
    def is_images_have_same_size(images: list[WebElement]) -> bool:
        """
        Проверка равенства размеров всех изображений в блоке "Работаем"
        :param images: Изображения, размер которых надо проверить
        :return: True, если размер всех изображений одинаковый, иначе False
        """
        if not images:
            return True
        width = images[0].size.get('width')
        height = images[0].size.get('height')
        logger.info(f"Размер всех изображений должен быть равен: {width} * {height}")
        for image in images:
            curr_width = image.size.get('width')
            curr_height = image.size.get('height')
            if curr_width != width or curr_height != height:
                logger.error(f"Найдено изображение с иным размером: {curr_width} * {curr_height}")
                return False
        logger.info("Все изображения одинакового размера")
        return True

    images_container = page.we_are_working_images_container
    page.wait_until(expected_conditions.visibility_of(images_container))

    we_are_working_images = page.we_are_working_images
    assert is_images_have_same_size(we_are_working_images)


def verify_power_in_people_url_changes_after_click(page: TensorPage):
    """
    Проверка смены url при нажатии по ссылке в блоке "Сила в людях"
    :param page: Главная страница сайта Тензор
    :return: None
    """
    url = page.browser.current_url
    button = page.power_in_people_more_button

    page.wait_until(expected_conditions.visibility_of(button))

    page.browser.execute_script("arguments[0].scrollIntoView();", button)
    ActionChains(page.browser).move_to_element(button).click().perform()

    page.wait_until(expected_conditions.url_changes(url))

    assert page.browser.current_url == TENSOR_ABOUT_PAGE_URL


def verify_power_in_people_text(page: TensorPage):
    """
    Валидация текста в блоке "Сила в людях"
    :param page: Главная страница сайта Тензор
    :return: None
    """
    power_text = page.power_in_people_text
    page.wait_until(expected_conditions.visibility_of(power_text))

    assert (power_text.text is not None) and power_text.text == POWER_IN_PEOPLE_LABEL


def click_contacts(page: SbisPage):
    """
    Осуществление клика на ссылку "Контакты"
    :param page: Главная страница Сбис
    :return: None
    """
    contacts_link = page.header_contacts_link
    page.wait_until(expected_conditions.element_to_be_clickable(contacts_link))
    ActionChains(page.browser).click(contacts_link).perform()


def click_on_tensor_image(page: SbisPage, logger: Logger):
    """
    Осуществление клика на изображение логотипа Тензора
    :param page: Главная страница Сбис
    :return: None
    """
    image = page.tensor_image
    # ждём, когда логотип Тензора станет кликабельным
    page.wait_until(expected_conditions.element_to_be_clickable(image))
    # кликаем по нему
    ActionChains(page.browser).click(image).perform()

    logger.warning("После клика по ссылке открывается новая владка, возвращаемся на предыдующую вкладку")
    # после клика открывается новая владка, поэтому мы возвращаемся на первую вкладку
    page.browser.switch_to.window(page.browser.window_handles[0])


@mark.scenario_1
def test_scenario_1(initialized_browser, logger):
    logger.info(f"Открываем страницу {SBIS_PAGE_URL}")
    # открываем страницу Сбис
    sbis_page = SbisPage(initialized_browser)
    sbis_page.open()

    logger.info("Переходим во вкладку \"Контакты\"")
    # Кликаем на ссылку "Контакты"
    click_contacts(sbis_page)

    logger.info(f"Нажимаем на логотип компании \"Тензор\" и переходим на {TENSOR_SITE_URL}")
    # Кликаем на логотип Тензора
    click_on_tensor_image(sbis_page, logger)

    tensor_page = TensorPage(initialized_browser)
    tensor_page.open()

    logger.info("Проверка наличия на странице блока \"Сила в людях\"")
    # Проверяем наличие блока "Сила в людях"
    verify_power_in_people_text(tensor_page)

    logger.info("Переход по ссылке в блоке \"Сила в людях\"")
    # Переходим по ссылке, указанной в этом блоке и проверяем url
    verify_power_in_people_url_changes_after_click(tensor_page)

    tensor_about_page = TensorAboutPage(initialized_browser)
    tensor_about_page.open()

    logger.info("Валидация изображений в блок \"работаем\"")
    # валидация изображений в блоке "работаем"
    verify_we_are_working_images(tensor_about_page, logger)
