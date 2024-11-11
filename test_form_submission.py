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

# Test gửi form với thông tin không hợp lệ và hợp lệ
def test_form_submission(driver):
    # Điều hướng đến trang đăng nhập
    driver.get("https://demo-opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(10)  # Chờ trang tải hoàn toàn

    # Nhập thông tin không hợp lệ
    driver.find_element(By.NAME, "firstname").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # Tên không hợp lệ
    driver.find_element(By.NAME, "lastname").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # Họ không hợp lệ
    driver.find_element(By.NAME, "email").send_keys("nhan123@gmail.com")  # Email không hợp lệ
    driver.find_element(By.NAME, "password").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # Mật khẩu quá dài
    time.sleep(4)
    driver.find_element(By.NAME,"agree").click()
    time.sleep(4)
    submit_button = driver.find_element(By.XPATH, "//*[@id='form-register']/div/button")
    submit_button.click()
    time.sleep(3)
    error_firstname = driver.find_element(By.ID,"error-firstname")
    error_lastname = driver.find_element(By.ID,"error-lastname")
    error_password = driver.find_element(By.ID,"error-password")
    error_email = driver.find_element(By.ID,"alert")
    # Kiểm tra thông báo lỗi hiển thị cho từng trường
    assert "Warning: E-Mail Address is already registered!" == error_email.text
    assert "First Name must be between 1 and 32 characters!" == error_firstname.text
    assert "Last Name must be between 1 and 32 characters!" == error_lastname.text
    assert "Password must be between 4 and 20 characters!" == error_password.text

    # Làm mới trang và nhập thông tin hợp lệ
    time.sleep(3)

    
