from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest

def test_register():
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    # passing driver object to constructer in RegistrationPage
    register = RegistrationPage.Registration(driver)
    register.enter_userame("hello")
    register.enter_password("hello")
    InitiateDriver.closeBrowser()