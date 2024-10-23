from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest 

options = Options()
options.add_argument("--headless=new")

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()