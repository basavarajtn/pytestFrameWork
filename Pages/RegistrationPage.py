from Library import ConfigReader

class Registration:
    def __init__(self,obj):
        global driver
        driver=obj

    def enter_userame(self, username):
        driver.find_element_by_name(ConfigReader.featchElementLocators("Registration", "username_name")).send_keys(
            username)

    def enter_password(self, password):
        driver.find_element_by_name(ConfigReader.featchElementLocators("Registration", "password_name")).send_keys(
            password)

    def enter_email(self, email):
        driver.find_element_by_name(ConfigReader.featchElementLocators("Registration", "email_name")).send_keys(
            email)