import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.custome_logger import Log_maker

from base_pages.Creat_Administor import Create_Administrator
import os
from dotenv import load_dotenv
load_dotenv()
class Test_03_Administrator:
    admin_page_url = os.getenv('url')
    username = os.getenv('superadmin')
    password = os.getenv('password')
    invalid_username = os.getenv('invalid_username')
    logger = Log_maker.log_gen()


    def test_create_administrator(self,setup):
        self.driver = setup
        self.logger.info("###test_valid_admin_login####")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        #time.sleep(5)
        self.logger.info("****Opening URL****")

        self.admin_create = Create_Administrator(self.driver)
        self.admin_create.enter_username(self.username)
        self.admin_create.enter_password(self.password)
        self.admin_create.click_login()
        self.admin_create.click_accept()
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Administrators']")))
        self.admin_create.click_administrator()
        self.admin_create.click_create_administrator()
        self.admin_create.enter_first_name("Testauto")
        self.admin_create.enter_last_name("Test123")
        self.admin_create.enter_username_administrator("testuserauto")
        self.admin_create.enter_email("testauto@yopmai.com")
        self.admin_create.enter_location("SouthAfrica")
        self.admin_create.click_save()









