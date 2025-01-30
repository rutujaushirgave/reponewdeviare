from selenium.webdriver.common.by import By


class Create_Administrator:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='kc-login']"
    Administrator_xpath = "//p[normalize-space()='Administrators']"
    Create_Administrator_xpath = "//span[normalize-space()='Create Administrator']"
    First_Name_xpath = "//input[@placeholder='First Name']"
    Last_Name_xpath = "//input[@placeholder='Last Name']"
    username_xpath = "//input[@placeholder='Username']"
    email_xpath = "//input[@placeholder='Email']"
    location_xpath = "//input[@placeholder='Location']"
    save_xpath = "//button[normalize-space()='Save']"
    accept_btn_xpath = "//a[@id='hs-eu-confirmation-button']"



    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_administrator(self):
        self.driver.find_element(By.XPATH,self.Administrator_xpath).click()

    def click_create_administrator(self):
        self.driver.find_element(By.XPATH,self.Create_Administrator_xpath).click()

    def enter_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.First_Name_xpath).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.Last_Name_xpath).send_keys(last_name)

    def enter_username_administrator(self,username_admin):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username_admin)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def enter_location(self,location):
        self.driver.find_element(By.XPATH,self.location_xpath).send_keys(location)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()

    def click_accept(self):
        self.driver.find_element(By.XPATH,self.accept_btn_xpath).click()



