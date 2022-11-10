from selenium import webdriver
from selenium.webdriver.common.by import By

class AccountPageClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_DeleteAccount_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteMainBtnContainer")

    def Click_DeleteAccount(self):
        self.Get_DeleteAccount_Element().click()

    def Get_GetDeleteButton_Element(self):
        return self.driver.find_element(By.CLASS_NAME,"deleteRed")

    def Click_DeleteButton(self):
        self.Get_GetDeleteButton_Element().click()

    def Get_GetCloseButton_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteRed")

    def Click_CloseButton(self):
        self.Get_GetDeleteButton_Element().click()
