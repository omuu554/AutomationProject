from selenium import webdriver
from selenium.webdriver.common.by import By


class Category_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product(self, product_id: int):
        return self.driver.find_element(By.ID, f"{product_id}")
    def product_name(self, product_id: int):
        return self.driver.find_element(By.XPATH, f"//img[@id='{product_id}']/../p[1]/a")

    def product_price(self, product_id: int):
        return self.driver.find_element(By.XPATH, f"//img[@id='{product_id}']/../p[2]/a")

    def click_product(self, product_id: int):
        self.product(product_id).click()