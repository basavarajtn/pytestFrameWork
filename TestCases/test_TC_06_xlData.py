from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
from dataGenarator import xlsDataGen
import openpyxl

@pytest.mark.parametrize('data',xlsDataGen.xlsdata())
def test_invaliddata(data):
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    register = RegistrationPage.Registration(driver)  #passing driver object to constructer in RegistrationPage
    register.enter_userame(data[0])
    register.enter_password(data[1])
    InitiateDriver.closeBrowser()