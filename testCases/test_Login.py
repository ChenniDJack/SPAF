import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    userName = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        title = self.driver.title
        self.driver.close()
        if title == "Your store. Login":
            assert True
        else:
            assert False


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title
        self.driver.close()
        if title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False





