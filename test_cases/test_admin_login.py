import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.custome_logger import Log_maker
import os
from dotenv import load_dotenv
load_dotenv()

class Test_01_Admin_Login:
    admin_page_url = os.getenv('url')
    username = os.getenv('superadmin')
    password = os.getenv('password')
    invalid_username = os.getenv('invalid_username')
    logger = Log_maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.driver = setup
        self.logger.info("####test_title_verification###")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        time.sleep(5)
        act_title = self.driver.title

        exp_title = "Log in to Deviare SSO"
        if act_title == exp_title:
            self.logger.info("************Title match************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\Dell\\PycharmProjects\\Deviare_new_framework\\pythonProject\\screenshots\\test_verification.png")
            self.logger.info("************Title not match************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.logger.info("###test_valid_admin_login####")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("****Opening URL****")
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.logger.info("****Entering Username****")
        self.admin_lp.enter_password(self.password)
        self.logger.info("****Entering password****")
        self.admin_lp.click_login()
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Dashboard']")))

        act_platform_text = self.driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").text
        if act_platform_text == "Dashboard":
            self.logger.info("************Platform_finded************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\Dell\\PycharmProjects\\Deviare_new_framework\\pythonProject\\screenshots\\test_valid_admin_login1.png")
            self.driver.close()
            assert False
#####


