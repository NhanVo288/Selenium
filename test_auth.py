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

# Test đăng nhập với thông tin hợp lệ
def test_login_valid(driver):
    driver.get("https://demo.opencart.com/")  # Truy cập trang chủ
    time.sleep(10)  # Chờ trang tải xong
    WebDriverWait(driver, 10).until(EC.url_to_be("https://demo.opencart.com/"))  # Đợi cho đến khi URL chính xác
    # Tìm và click vào menu dropdown
    menu_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a")))
    menu_dropdown.click()
    # Tìm và click vào link đăng nhập
    login_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']")))
    login_link.click()
    # Nhập thông tin đăng nhập và submit
    driver.find_element(By.NAME, "email").send_keys("nhan123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

# Test đăng nhập với thông tin không hợp lệ
def test_login_invalid(driver):
    # Truy cập trang chủ của OpenCart
    driver.get("https://demo.opencart.com/")
    time.sleep(10)  # Chờ 10 giây để trang tải hoàn toàn
    # Đợi cho đến khi URL trang chủ được tải xong
    WebDriverWait(driver, 10).until(EC.url_to_be("https://demo.opencart.com/"))
    # Tìm và click vào menu dropdown của tài khoản người dùng
    menu_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a")))
    menu_dropdown.click()
    # Tìm và click vào link đăng nhập
    login_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']")))
    login_link.click()
    time.sleep(3)  # Chờ 3 giây để form đăng nhập hiển thị
    # Nhập email và mật khẩu không hợp lệ
    driver.find_element(By.NAME, "email").send_keys("nhan123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(3)  # Chờ 3 giây trước khi nhấn nút đăng nhập
    # Nhấn nút đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)  # Chờ 3 giây để xử lý đăng nhập
    # Kiểm tra thông báo lỗi hiển thị khi đăng nhập thất bại
    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "alert")))
    assert "Warning: No match for E-Mail Address and/or Password." in message.text
    submit_button.click()
    time.sleep(3)  # Chờ 3 giây để xử lý đăng nhập
    # Kiểm tra thông báo lỗi hiển thị khi đăng nhập thất bại
    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "alert")))
    assert "Warning: No match for E-Mail Address and/or Password." in message.text

def test_login_empty_email_password(driver):
    # Truy cập trang chủ của OpenCart
    driver.get("https://demo.opencart.com/")
    time.sleep(10)  # Chờ 10 giây để trang tải hoàn toàn
    # Đợi cho đến khi URL trang chủ được tải xong
    WebDriverWait(driver, 10).until(EC.url_to_be("https://demo.opencart.com/"))
    # Tìm và click vào menu dropdown của tài khoản người dùng
    menu_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a")))
    menu_dropdown.click()
    # Tìm và click vào link đăng nhập
    login_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']")))
    login_link.click()
    time.sleep(3)  # Chờ 3 giây để form đăng nhập hiển thị
    # Nhấn nút đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)  # Chờ 3 giây để xử lý đăng nhập
    # Kiểm tra thông báo lỗi hiển thị khi đăng nhập thất bại
    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "alert")))
    assert "Warning: No match for E-Mail Address and/or Password." in message.text
    submit_button.click()
    time.sleep(3)  # Chờ 3 giây để xử lý đăng nhập
    # Kiểm tra thông báo lỗi hiển thị khi đăng nhập thất bại
    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "alert")))
    assert "Warning: No match for E-Mail Address and/or Password." in message.text

# Test đăng xuất
def test_logout(driver):
    # Điều hướng đến trang đăng nhập
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(10)  # Chờ trang tải hoàn toàn

    # Nhập địa chỉ email vào trường nhập email
    driver.find_element(By.NAME, "email").send_keys("nhan123@gmail.com")
    # Nhập mật khẩu vào trường nhập mật khẩu
    driver.find_element(By.NAME, "password").send_keys("123456")

    # Tìm và nhấn nút đăng nhập để gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)
    # Chờ đợi cho đến khi menu dropdown của người dùng có thể nhấn vào và sau đó nhấn vào đó
    menu_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a")))
    menu_dropdown.click()

    # Chờ đợi cho đến khi liên kết đăng xuất có thể nhấn vào và sau đó nhấn vào đó để đăng xuất
    logout_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']")))
    logout_link.click()