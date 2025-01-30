from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


class Create_New_user:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='kc-login']"
    accept_btn_xpath = "//a[@id='hs-eu-confirmation-button']"
    users_btn_xpath = "//p[normalize-space()='Users']"
    create_user_btn_xpath = "//span[normalize-space()='Create User']"
    first_name_textbox_xpath = "//input[@placeholder='First Name']"
    surname_textbox_xpath = "//input[@placeholder='Last Name']"
    username_textbox_xpath = "//input[@placeholder='Username']"
    email_textbox_xpath = "//input[@placeholder='Email']"
    company_name_dropdown_xpath = "//input[@id='tags-outlined']"
    select_company_dropdown_xpath = "//li[@id='tags-outlined-option-47']"
    role_dropdown_xpath = "//div[@id='select-outlined-Select Role']"
    select_role_xpath = "//li[normalize-space()='User']"
    location_textbox_xpath = "//input[@placeholder='Location']"
    save_btn_xpath = "//span[normalize-space()='Save']"

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

    def click_users(self):
        self.driver.find_element(By.XPATH, self.users_btn_xpath).click()

    def click_create_users(self):
        self.driver.find_element(By.XPATH, self.create_user_btn_xpath).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name_textbox_xpath).send_keys(firstname)

    def enter_surname(self, surname):
        self.driver.find_element(By.XPATH, self.surname_textbox_xpath).send_keys(surname)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(email)

    def click_company_name(self):
        self.driver.find_element(By.XPATH, self.company_name_dropdown_xpath).click()
    def select_company_name(self):
        self.driver.find_element(By.XPATH, self.select_company_dropdown_xpath).click()


    def select_role(self):
        self.driver.find_element(By.XPATH, self.role_dropdown_xpath).click()

    def select_user_role(self):
        self.driver.find_element(By.XPATH, self.select_role_xpath).click()

    def enter_location(self, location):
        self.driver.find_element(By.XPATH, self.location_textbox_xpath).send_keys(location)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()


