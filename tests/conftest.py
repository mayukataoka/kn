import pytest
import os
import sys
from selenium import webdriver


@pytest.fixture(scope="class", autouse=True)
def setup_driver(request):
    global driver
    DRIVER_PATH = '/Users/mayukataoka/Downloads/chromedriver'
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.implicitly_wait(10)
    URL = 'https://www.khanacademy.org/'
    driver.get(URL)
    request.cls.driver = driver
    yield driver
    driver.close()


