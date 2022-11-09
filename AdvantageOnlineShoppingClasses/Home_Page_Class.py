from selenium import webdriver
from selenium.webdriver.common.by import By


class Home_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def category(self, category_name: str):
        return self.driver.find_element(By.ID, f"{category_name}Img")

    def click_category(self, category_name: str):
        self.category(category_name).click()