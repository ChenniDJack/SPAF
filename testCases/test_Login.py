import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:

        self.driver.get(self.baseURL)
        title = self.driver.title
            self.driver.close()
        else:
            assert False


        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        title = self.driver.title
            self.driver.close()
        else:
            assert False





