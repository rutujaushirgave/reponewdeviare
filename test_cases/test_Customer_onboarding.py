import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.custome_logger import Log_maker

from base_pages.CustomerOnboarding import Customer_Onboarding
import os
from dotenv import load_dotenv
load_dotenv()

class Test_03_Administrator:
    admin_page_url = os.getenv('url')
    username = os.getenv('superadmin')
    password = os.getenv('password')
    invalid_username = os.getenv('invalid_username')
    logger = Log_maker.log_gen()

    def test_Customer_Onboarding(self, setup):
        self.driver = setup
        self.logger.info("###test_valid_admin_login####")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.customer_onboard = Customer_Onboarding(self.driver)
        self.customer_onboard.enter_username(self.username)
        self.customer_onboard.enter_password(self.password)
        self.customer_onboard.click_login()
        self.customer_onboard.click_accept()
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Administrators']")))
        self.customer_onboard.click_Customer_Onboard()
        self.customer_onboard.enter_company("testcompnay")
        self.customer_onboard.enter_email("testcopmany@yopmail.com")
        self.customer_onboard.enter_address("southAfrica")
        #self.customer_onboard.select_country("India")
        #time.sleep(5)
        self.customer_onboard.select_account_type()
        self.customer_onboard.acc_value()
        self.customer_onboard.enter_phone_Number("+911231233333")
        time.sleep(5)

