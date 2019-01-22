from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import Locators
from selenium.webdriver.support.ui import Select

from pages.header import Header
from selenium.webdriver.support import expected_conditions as ec

from pages.personalize_ka import Personalize
class Signup:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)

    def join_ka(self, status, email, username, password):

        self.header.open_sign_up()

        if status == 'learner':
           self.driver.find_element_by_xpath(Locators.sign_up_learner_button_xpath).click()


        self.driver.find_element_by_xpath(Locators.sign_up_learner_button_xpath).click()
        Select(self.driver.find_element_by_id(Locators.month_birthday_picker_dropdown_id)).select_by_value('1')

        Select(self.driver.find_element_by_id(Locators.day_birthday_picker_dropdown_id)).select_by_value('1')
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, Locators.year_birthday_picker_dropdown_id)))
        Select(self.driver.find_element_by_id(Locators.year_birthday_picker_dropdown_id)).select_by_value('2019')
        self.driver.find_element_by_xpath(Locators.sign_up_with_email_button_xpath).click()
        self.driver.find_element_by_id(Locators.email_id).send_keys(email)
        self.driver.find_element_by_id(Locators.username_id).send_keys(username)
        self.driver.find_element_by_id(Locators.password_id).send_keys(password)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.sign_up_button_css)))
        self.driver.find_element_by_css_selector(Locators.sign_up_button_css).click()

        return Personalize(self.driver)



