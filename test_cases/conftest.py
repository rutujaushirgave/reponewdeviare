import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    # This will automatically handle downloading and setting the correct version of chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()  # Ensure to close the browser after the test





# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
