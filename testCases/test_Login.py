import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # userName = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    # l = LogGen()
    # l.loggen()

    lg = LogGen()
    logger = lg.loggen()
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        if title == "Welcome: Mercury Tour":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title
        if title == "Login: Mercury Tours":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False