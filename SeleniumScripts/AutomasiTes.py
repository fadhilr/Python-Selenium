from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.set_page_load_timeout(30)
driver.get("http://localhost/webklinik/")
driver.maximize_window()
driver.implicitly_wait(20)
assert "Login" in driver.title
driver.get_screenshot_as_file("./Screenshots/WebKlinik.png")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_id("saveForm").click()
driver.get_screenshot_as_file("./Screenshots/AdminDashboard.png")

time.sleep(5)
driver.quit()

print("Test completed successfully")