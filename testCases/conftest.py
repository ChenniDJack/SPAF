from selenium import webdriver
import pytest
from utilities.customLogger import LogGen

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture(autouse=True)
def log_setup():
    # createLog()  # Initialize logging before any tests
    logger = LogGen.loggen()  # Initialize custom logger
    return logger