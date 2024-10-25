from selenium import webdriver
import pytest
from utilities.customLogger import LogGen

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

