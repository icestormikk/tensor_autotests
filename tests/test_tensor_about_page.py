import pytest

from pages.tensor_about_page import TensorAboutPage, is_images_have_same_size


@pytest.mark.scenario_1
def test_we_are_working_same_size(initialized_browser):
    tensor_about_page = TensorAboutPage(initialized_browser)
    images = tensor_about_page.we_are_working_images

    assert is_images_have_same_size(images)