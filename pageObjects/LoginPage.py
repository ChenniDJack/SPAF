class LoginPage:

    username_textbox_name = "userName"
    password_textbox_name = "password"
    submit_button_name = "submit"

    Logout_button_xpath = "//a[text()='SIGN-OFF']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element('name', self.username_textbox_name).clear()
        self.driver.find_element('name', self.username_textbox_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element('name', self.password_textbox_name).clear()
        self.driver.find_element('name', self.password_textbox_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("name", self.submit_button_name).click()

    def clickLogout(self):
        self.driver.find_element("xpath", self.Logout_button_xpath).click()