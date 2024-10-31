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

# Test gửi form với thông tin không hợp lệ
def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(10)
    driver.find_element(By.NAME, "email").send_keys("nhan123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(3)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "alert")))
    assert "Warning: No match for E-Mail Address and/or Password." in message.text

# Test điều hướng trang
def test_navigation(driver):
    driver.get("https://demo.opencart.com/home")
    time.sleep(10)
    about_us_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "About Us")))
    about_us_link.click()
    assert "About Us" in driver.title
    contact_us_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Contact Us")))
    contact_us_link.click()
    assert "Contact Us" in driver.title

# Test xác thực dữ liệu sản phẩm
def test_data_validation(driver):
    driver.get("https://demo.opencart.com/home")
    time.sleep(10)
    macbook_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='MacBook']")))
    assert macbook_element.text == "MacBook", "Tên sản phẩm đúng!"
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    assert macbook_price_element.text == "$602.00", "Giá của MacBook đúng!"
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")
    assert "Intel Core 2 Duo processor" in macbook_description_element.text, "Mô tả chứa thông tin mong đợi!"
    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")

# Test thêm vào giỏ hàng và thanh toán
def test_add_to_cart_and_checkout(driver):
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
    

# Test tìm kiếm sản phẩm hợp lệ
def test_search_valid_functionality(driver):
    # Truy cập trang chủ của OpenCart
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    # Tìm kiếm hộp nhập liệu tìm kiếm và nhập từ khóa "Iphone"
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Iphone")
    # Chờ đợi cho đến khi nút tìm kiếm trở nên có thể nhấp vào và thực hiện hành động click
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")))
    search_button.click()
    # Kiểm tra xem tiêu đề trang có chứa từ khóa tìm kiếm không, để xác nhận rằng trang tìm kiếm đã được tải đúng
    assert "Search - Iphone" in driver.title

# Test tìm kiếm sản phẩm không hợp lệ
def test_search_invalid_functionality(driver):
    driver.get("https://demo.opencart.com/")
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

# Test thiết kế đáp ứng với các kích thước màn hình khác nhau
@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])
def test_responsive_design(driver, size):
    driver.set_window_size(*size)  # Thiết lập kích thước cửa sổ
    driver.get("https://demo.opencart.com/")
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logo")))  # Kiểm tra logo hiển thị
    assert logo.is_displayed()  # Xác nhận logo được hiển thị
