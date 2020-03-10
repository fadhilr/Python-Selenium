import unittest

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class LoginWebKlinik(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        username = "admin"
        password = "1234"

        usernameFieldId = "username"
        passwordFieldId = "password"

        usernameFieldElement = driver.find_element_by_id(usernameFieldId)
        passwordFieldElement = driver.find_element_by_id(passwordFieldId)
        loginButtonElement = driver.find_element_by_id("saveFrom")
        usernameFieldElement.clear()
        usernameFieldElement.send_keys(username)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)
        loginButtonElement.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
