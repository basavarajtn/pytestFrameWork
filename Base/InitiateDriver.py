from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

def openBrowser():
    global driver
    if ((ConfigReader.readConfigData('Details','Browser'))== "Chrome"):
        path="./Drivers/chromedriver.exe"
        driver=Chrome(executable_path=path)
    elif ((ConfigReader.readConfigData('Details','Browser'))== "Firefox"):
        path = "./Drivers/geckodriver.exe"
        driver = Firefox(executable_path=path)
    else:
        path = "./Drivers/chromedriver.exe"
        driver = Chrome(executable_path=path)
    driver.maximize_window()
    return driver

def openApplication():
    driver.get(ConfigReader.readConfigData('Details','ApplicationURL'))

def closeBrowser():
    driver.close()