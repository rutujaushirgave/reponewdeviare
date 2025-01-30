import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.custome_logger import Log_maker

from base_pages.CreatingUser import Create_New_user
from base_pages.CustomerOnboarding import Customer_Onboarding
import os
from dotenv import load_dotenv
load_dotenv()



class Test_04_create_user:
    admin_page_url = os.getenv('url')
    username = os.getenv('superadmin')
    password = os.getenv('password')
    invalid_username = os.getenv('invalid_username')
    logger = Log_maker.log_gen()

    def test_create_new_user(self, setup):
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
        self.create_user = Create_New_user(self.driver)
        self.create_user.click_users()
        self.create_user.click_create_users()
        self.create_user.enter_first_name("jantest12")
        self.create_user.enter_surname("jantest12")
        self.create_user.enter_username("jantest12")
        self.create_user.enter_email("jantest12@yopmail.com")
        self.create_user.click_company_name()
        self.create_user.select_company_name()
        self.create_user.select_role()
        self.create_user.select_user_role()
        self.create_user.enter_location("India")
        self.create_user.click_save()
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[normalize-space()='Users']")))
        user_added_text = self.driver.find_element(By.XPATH, "//h4[normalize-space()='Users']").text
        user_added_text = self.driver.find_element(By.XPATH, "//h4[normalize-space()='Users']").text
        if "User" in user_added_text:
            assert True
            self.driver.quit()

        else:
            self.driver.save_screenshot("C:\\Users\\Dell\\PycharmProjects\\Deviare_new_framework\\pythonProject\\screenshots\\screenshot1.png")
            self.driver.quit()
            assert False









