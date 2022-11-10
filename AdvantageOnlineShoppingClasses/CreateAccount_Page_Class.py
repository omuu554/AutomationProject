from selenium import webdriver
from selenium.webdriver.common.by import By

class CreateAccountClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_UserName_Element(self):
        "Returns the element of THE USERNAME"
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def Get_Email_Element(self):
        "Returns the element of THE EMAIL"
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def Get_Password_Element(self):
        "Returns the element of THE PASSWORD"
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def Get_ConfirmPassword_Element(self):
        "Returns the element of THE CONFIRM PASSWORD"
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def Get_IAgree_Element(self):
        "Returns the element of THE IAGREE checkbox"
        return self.driver.find_element(By.NAME, "i_agree")

    def Get_RegisterButton_Element(self):
        "Returns the element of THE REGISTER button"
        return self.driver.find_element(By.ID, "register_btnundefined")

    def Click_RegisterButton(self):
        "Clicks on REGISTER button"
        self.Get_RegisterButton_Element().click()

    def IsIAgree_Selected(self):
        return self.Get_IAgree_Element().is_selected()