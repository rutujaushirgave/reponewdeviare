from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


class Customer_Onboarding:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='kc-login']"
    accept_btn_xpath = "//a[@id='hs-eu-confirmation-button']"
    customerOnboarding_xpath = "//p[normalize-space()='Customer Onboarding']"
    companyName_xpath = "//input[@placeholder='Company Name']"
    email1_xpath = "//input[@placeholder='Email']"
    address_xpath = "//input[@placeholder='Address']"
    countryRegistraion_xpath = "//input[@id='combo-box-demo4']"
    selectAccount_xpath = "//*[@id='select-outlined-Accout Type']"
    account_type_value = "//li[normalize-space()='Enterprise Customer']"
    phone_xpath = "//input[@placeholder='1 (702) 123-4567']"
    upload_logo = "//input[@id='file-input']"
    next_xpath = "//button[@type='button'][normalize-space()='Next']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_accept(self):
        self.driver.find_element(By.XPATH, self.accept_btn_xpath).click()

    def click_Customer_Onboard(self):
        self.driver.find_element(By.XPATH, self.customerOnboarding_xpath).click()

    def enter_company(self, company):
        self.driver.find_element(By.XPATH, self.companyName_xpath).send_keys(company)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email1_xpath).send_keys(email)

    def enter_address(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def select_country(self, country):
        self.driver.find_element(By.XPATH, self.countryRegistraion_xpath).send_keys(country)

    def select_account_type(self):
        self.driver.find_element(By.XPATH, self.selectAccount_xpath).click()

    def acc_value(self):
        self.driver.find_element(By.XPATH,self.account_type_value).click()

    def enter_phone_Number(self, value):
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(value)
