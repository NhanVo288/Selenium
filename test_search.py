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

# Test tìm kiếm sản phẩm hợp lệ
def test_search_valid_functionality(driver):
    # Truy cập trang chủ của OpenCart
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    # Tìm kiếm hộp nhập liệu tìm kiếm và nhập từ khóa "Iphone"
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("iPhone")
    # Chờ đợi cho đến khi nút tìm kiếm trở nên có thể nhấp vào và thực hiện hành động click
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    time.sleep(4)
    name = driver.find_element(By.XPATH,"//*[@id='product-list']/div/div/div[2]/div/h4/a")
    assert name.text == "iPhone" # Kiểm tra xem có sản phẩm liên quan không

# Test tìm kiếm sản phẩm không hợp lệ
def test_search_invalid_functionality(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("asdasd")
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    # Chờ đợi thông báo sản phẩm không tìm thấy
    no_product_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content p")))
    # Kiểm tra thông báo không tìm thấy sản phẩm
    assert "There is no product that matches the search criteria." in no_product_message.text

# Test tìm kiếm với từ khóa có độ dài lớn
def test_search_long_keyword(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("a" * 1000)  # Nhập từ khóa rất dài
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    no_product_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content p")))
    # Kiểm tra thông báo không tìm thấy sản phẩm
    assert "There is no product that matches the search criteria." in no_product_message.text

# Test tìm kiếm với từ khóa giống một phần kết quả
def test_search_partial_match_keyword(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Phone")  # Nhập từ khóa là một phần của sản phẩm có sẵn
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    name = driver.find_element(By.XPATH,"//*[@id='product-list']/div/div/div[2]/div/h4/a")
    time.sleep(4)
    assert name.text == "iPhone" # Kiểm tra xem có sản phẩm liên quan không

# Test tìm kiếm với từ khóa có chữ hoa, chữ thường
def test_search_case_insensitivity(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("IPHONE")  # Nhập từ khóa bằng chữ hoa
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    time.sleep(5)
    name = driver.find_element(By.XPATH,"//*[@id='product-list']/div/div/div[2]/div/h4/a")
    assert name.text == "iPhone" # Kiểm tra xem có sản phẩm liên quan không

# Test tìm kiếm với kí tự đặc biệt 
def test_search_special_characters(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("@#$%^&*")  # Nhập kí tự đặc biệt 
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    # Chờ đợi thông báo sản phẩm không tìm thấy
    no_product_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content p")))
    # Kiểm tra thông báo không tìm thấy sản phẩm
    assert "There is no product that matches the search criteria." in no_product_message.text

# Test tìm kiếm với kí tự số
def test_search_numeric_characters(driver):
    driver.get("https://demo-opencart.com/")
    time.sleep(10)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("123456")  # Nhập kí tự số
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
     # Chờ đợi thông báo sản phẩm không tìm thấy
    no_product_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content p")))
    # Kiểm tra thông báo không tìm thấy sản phẩm
    assert "There is no product that matches the search criteria." in no_product_message.text