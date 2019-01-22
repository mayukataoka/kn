from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.locators import Locators


class Personalize:

    def __init__(self, driver):
        self.driver = driver

    def is_popup_dialog_visible(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, Locators.ka_popup_header_xpath)))
        return self.driver.find_element_by_xpath(Locators.ka_popup_header_xpath).is_displayed()
