from POMProjectDemo.Locators.locators import Locators


class KaryawanPage():

    def __init__(self, driver):
        self.driver = driver

        self.keluar_link_id = Locators.keluar_link_id

    def click_keluar(self):
        self.driver.find_element_by_link_text(self.keluar_link_id).click()
