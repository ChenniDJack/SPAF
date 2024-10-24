from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.driver_finder import logger

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getPassword()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*********************Test_001_Login***************")
        self.logger.info("*********************Verifying Home Page Title***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title

        if title == "Welcome: Mercury Tours":
            assert True
            self.driver.close()
            self.logger.info("*********************Home page title test is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********************Home page title test is failed***************")
            assert False



    def test_login(self, setup):
        self.logger.info("*********************Verifying Login Test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.userName)
        self.lp.set_password(self.password)
        self.lp.click_login()
        title = self.driver.title
        if title == "Login: Mercury":
            assert True
            self.driver.close()
            self.logger.info("*********************Login test is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*********************Login test is failed***************")
            assert False





