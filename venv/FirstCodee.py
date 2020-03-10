from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert  "No result found" not in driver.page_source
time.sleep(5)

driver.get("http://www.google.com")

# assert "penelusuran google" in driver.title

driver.find_element_by_name("q").send_keys("automation step by step")
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys("test automation")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()

print("Test completed successfully")