from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest

def staticDataGenrator():
    li=[['username1','pass1','mailid1@test.com'],['username2','pass2','mailid2@test.com'],['username3','pass3','mailid3@test.com']]
    return li

@pytest.mark.parametrize('data',staticDataGenrator())
def test_invaliddata(data):
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    register = RegistrationPage.Registration(driver)  #passing driver object to constructer in RegistrationPage
    register.enter_userame(data[0])
    register.enter_password(data[1])
    register.enter_email(data[2])
    InitiateDriver.closeBrowser()