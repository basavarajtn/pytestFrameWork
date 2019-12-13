from Base import InitiateDriver
import pytest

def test_invaliddata():
    InitiateDriver.openBrowser()
    driver = InitiateDriver.openBrowser()
    InitiateDriver.openApplication()
    driver.find_element_by_name("fld_email").send_keys("testing@gmail.com")
    InitiateDriver.closeBrowser()