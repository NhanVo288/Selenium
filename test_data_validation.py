import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cài đặt trình điều khiển trước khi thực hiện các test
@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Sử dụng trình duyệt Edge
    driver.maximize_window()  # Phóng to cửa sổ trình duyệt
    yield driver
    driver.quit()  # Đóng trình duyệt sau khi test

# Test xác thực dữ liệu sản phẩm
def test_data_validation(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    macbook_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='MacBook']")))
    assert macbook_element.text == "MacBook", "Tên sản phẩm đúng!"
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    assert macbook_price_element.text == "$602.00", "Giá của MacBook đúng!"
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")
    assert "Intel Core 2 Duo processor" in macbook_description_element.text, "Mô tả chứa thông tin mong đợi!"
    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")