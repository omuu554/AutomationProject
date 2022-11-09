from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def category(self, category_name: str):
        """get category element by the name of the category """
        return self.driver.find_element(By.ID, f"{category_name}Img")


    def click_category(self, category_name: str):
        """go to category page by the name of the category"""
        self.category(category_name).click()
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".categoryTitle")))







