from pages.locators import Locators
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from pages.sign_up import Signup


class Header:

    def __init__(self, driver):
        self.driver = driver

    def open_sign_up(self):
        self.driver.find_element_by_link_text(Locators.header_sign_up_link_text).click()
        return Signup(self.driver)
