class LoginPage:

    username_textbox_id = "Email"
    password_textbox_id = "Password"
    submit_button_xpath = "//button[text()='Log in']"

    Logout_button_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.Logout_button_xpath).click()



