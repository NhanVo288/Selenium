import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Sử dụng trình duyệt Edge
    driver.maximize_window()  # Phóng to cửa sổ trình duyệt
    yield driver
    driver.quit()  # Đóng trình duyệt sau khi test


@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])
def test_responsive_design(driver, size):
    driver.set_window_size(*size)  # Thiết lập kích thước cửa sổ
    driver.get("https://demo-opencart.com/")
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logo")))  # Kiểm tra logo hiển thị
    assert logo.is_displayed()  # Xác nhận logo được hiển thị