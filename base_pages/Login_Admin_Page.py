from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='kc-login']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()