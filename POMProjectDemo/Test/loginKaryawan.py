from selenium import webdriver
import time
import unittest
import sys
import os
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.karyawanPage import KaryawanPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://localhost/webklinik/")

        login = LoginPage(driver)
        login.enter_username("karyawan2")
        login.enter_password("1234")
        login.click_login()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:/Users/fadil/PycharmProjects/Python Selenium/POMProjectDemo/Reports"))
