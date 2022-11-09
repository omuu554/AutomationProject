from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderPayment_page_NotLog_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def registration(self):
        return self.driver.find_element(By.ID,"registration_btnundefined")
    def click_registration(self):
        self.registration().click()

    def username(self):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")
    def tab_username(self, username: str):
        self.username().send_keys(f"{username}")
    def password(self):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")
    def tab_password(self, password: str):
        self.password().send_keys(f"{password}")

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    def click_login_button(self):
        self.login_button().click()