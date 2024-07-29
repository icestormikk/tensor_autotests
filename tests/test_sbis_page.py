import pytest

from pages.sbis_page import SbisPage


@pytest.mark.scenario_1
def test_sbis_page_contacts_logo(initialized_browser):
    sbis_page = SbisPage(initialized_browser)
    sbis_page.open()
    sbis_page.click_contacts()
    sbis_page.click_on_tensor_image()


def test_sbis_contacts_geo(initialized_browser):
    sbis_page = SbisPage(initialized_browser)
    sbis_page.open()