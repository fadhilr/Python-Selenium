from selenium import webdriver
import time
import unittest
import sys
import os
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProjectDemo.Pages.karyawanPage import KaryawanPage
from POMProjectDemo.Pages.loginPage import LoginPage


class PeriksaPasien(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_02_periksa_pasien_valid(self):
        driver = self.driver
        driver.get("http://localhost/webklinik/")

        login = LoginPage(driver)
        login.enter_username("karyawan2")
        login.enter_password("1234")
        login.click_login()

        driver.find_element_by_xpath("//tr[3]//td[5]//div[1]//a[3]").click()
        driver.find_element_by_xpath("//tr[1]//td[4]//input[1]").click()
        driver.find_element_by_xpath("//tr[3]//td[5]//input[1]").click()
        driver.find_element_by_xpath("//tr[11]//td[5]//input[1]").click()
        driver.find_element_by_xpath("//tr[21]//td[5]//input[1]").click()
        driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        driver.find_element_by_xpath("//li[2]//a[1]").click()

        karyawanPage = KaryawanPage(driver)
        karyawanPage.click_keluar()

        time.sleep(5)

    def test_01_login_karyawan_invalid(self):
        driver = self.driver
        driver.get("http://localhost/webklinik/")

        login = LoginPage(driver)
        login.enter_username("usernamesalah")
        login.enter_password("1234")
        login.click_login()
        time.sleep(5)
        driver.switch_to_alert().accept()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/fadil/PycharmProjects/Python Selenium/POMProjectDemo/Reports"))
