import configparser

def readConfigData(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/config.cfg")
    return config.get(section,key)

def featchElementLocators(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section,key)