from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class Cart_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    def product_name(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[2]/label")

    def product_color(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[4]/span")

    def product_quantity(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[5]/label[2]")

    def units_price(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[6]/p")

    def edit_product(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[6]/span/a[1]")

    def remove_product(self, product_location: int):
        return self.driver.find_element(By.XPATH, f"//thead/../tbody/tr[{product_location}]/td[6]/span/a[3]")

    def total_price(self):
        return self.driver.find_element(By.XPATH, "//thead/../tfoot/tr[1]/td[2]/span[2]")
    def check_Out_Button(self):
        return self.driver.find_element(By.ID, "checkOutButton")

    def continue_shopping(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='CONTINUE_SHOPPING']")

    def product_name_text(self, product_location: int):
        return self.product_name(product_location).text

    def product_color_name(self, product_location: int):
        return self.product_color(product_location).text

    def product_quantity_text(self, product_location: int):
        return self.product_quantity(product_location).text

    def units_price_text(self, product_location: int):
        return re.sub(r'[^0-9.]', '', self.units_price(product_location).text)

    def edit_product_click(self, product_location: int):
        self.edit_product(product_location).click()

    def remove_product_click(self, product_location: int):
        self.remove_product(product_location).click()

    def total_price_text(self):
        return re.sub(r'[^0-9.]', '', self.total_price().text)

    def check_Out_Button_click(self):
        self.check_Out_Button().click()

    def continue_shopping_click(self):
        self.continue_shopping().click()