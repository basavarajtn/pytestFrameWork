from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest

def test_invaliddata():
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    register = RegistrationPage.Registration(driver)  #passing driver object to constructer in RegistrationPage
    register.enter_userame("hello")
    register.enter_password("hello")
    register.enter_email("testing@gmail.com")
    InitiateDriver.closeBrowser()