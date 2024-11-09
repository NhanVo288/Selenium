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


def test_add_to_cart(driver):
    # Điều hướng đến trang chủ của trang demo
    driver.get("https://demo.opencart.com/")
    # Chờ 10 giây để đảm bảo trang được tải hoàn toàn
    time.sleep(10)
    # Chờ đợi cho đến khi nút 'Thêm vào giỏ hàng' có thể nhấp vào và sau đó nhấn vào nó
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]")))
    add_to_cart_button.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click()
    time.sleep(5)
    # Chờ đợi cho đến khi nút 'Thanh toán' trong dropdown giỏ hàng có thể nhấp vào và sau đó nhấn vào nó
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='header-cart']/div/ul/li/div/p/a[2]")))
    checkout_button.click()

def test_add_to_cart_invalid_quanity(driver):
    # Điều hướng đến trang chủ của trang demo
    driver.get("https://demo.opencart.com/")
    # Chờ 10 giây để đảm bảo trang được tải hoàn toàn
    time.sleep(10)
    # Chờ đợi cho đến khi nút 'Thêm vào giỏ hàng' có thể nhấp vào và sau đó nhấn vào nó
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]")))
    add_to_cart_button.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click()
    time.sleep(5)
    # Chờ đợi cho đến khi nút 'Thanh toán' trong dropdown giỏ hàng có thể nhấp vào và sau đó nhấn vào nó
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='header-cart']/div/ul/li/div/p/a[2]")))
    checkout_button.click()