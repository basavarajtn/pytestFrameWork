from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
import pytest


def test_register():
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    driver.find_element_by_name(ConfigReader.featchElementLocators("Registration","username_name")).send_keys("Hello")
    driver.find_element_by_name(ConfigReader.featchElementLocators("Registration","email_name")).send_keys("testing@gmail.com")
    InitiateDriver.closeBrowser()
