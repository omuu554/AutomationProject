from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderPayment_page_NotLog_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def registration(self):
        """get registration button element"""
        return self.driver.find_element(By.ID,"registration_btnundefined")
    def click_registration(self):
        """click on registration button"""
        self.registration().click()

    def username(self):
        """get username line element"""
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")
    def tab_username(self, username: str):
        """put the username in the line """
        self.username().send_keys(f"{username}")
    def password(self):
        """get the password line element"""
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")
    def tab_password(self, password: str):
        """put the password in the line"""
        self.password().send_keys(f"{password}")

    def login_button(self):
        """get the login button element"""
        return self.driver.find_element(By.ID, "login_btnundefined")

    def click_login_button(self):
        """click on login button"""
        self.login_button().click()