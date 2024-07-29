import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.tensor_page import TensorPage, TENSOR_ABOUT_PAGE_URL


@pytest.mark.scenario_1
def test_tensor_power_in_people_text(initialized_browser):
    tensor_page = TensorPage(initialized_browser)
    tensor_page.open()

    power_text = tensor_page.power_in_people_text
    assert power_text.text is not None


@pytest.mark.scenario_1
def test_tensor_power_in_people_button(initialized_browser):
    tensor_page = TensorPage(initialized_browser)
    tensor_page.open()

    url = tensor_page.browser.current_url

    tensor_page.click_on_power_in_people_more_button()

    WebDriverWait(tensor_page.browser, 10).until(
        expected_conditions.url_changes(url)
    )

    assert tensor_page.browser.current_url == TENSOR_ABOUT_PAGE_URL
