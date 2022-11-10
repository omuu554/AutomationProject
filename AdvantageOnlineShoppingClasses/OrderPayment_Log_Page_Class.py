from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re



class OrderPaymentLogClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Get_SelectedDetails_Element(self):
        "Returns the Element of the selected Detailels(Shipping/Payment)"
        return self.driver.find_element(By.CSS_SELECTOR,"#detailslink>label.selected")

    def SelectedDetailsName(self):
        "Returns a strings with the details name(Shipping/Payment)"
        return re.sub(r'[0-9. ]',"",self.Get_SelectedDetails_Element().text).replace(' ','')

    def Get_Next_Element(self):
        "Returns the Element of the Next button"
        return self.driver.find_element(By.ID,"next_btn")

    def Click_NextButton(self):
        "Clicks Next Button"
        self.Get_Next_Element().click()

    def Get_PaymentMethod_Element(self,index:int):
        "Returns the Element of the payment method by index"
        return self.driver.find_element(By.XPATH,f"//div[@class='paymentMethods']/div[{index}]")

    def Click_PaymentMethod(self,index:int):
        "Click on payment method by index"
        self.Get_PaymentMethod_Element(index).click()

    def Get_Username_Element(self):
        "Returns the Element of username of SafePay"
        return self.driver.find_element(By.NAME, "safepay_username")

    def Get_Password_Element(self):
        "Returns the Element of password of SafePay"
        return  self.driver.find_element(By.NAME, "safepay_password")

    def Get_SaveChangedCheckBoxSafePay_Element(self):
        "Returns the Element of SaveChanges CheckBox of SafePay"
        return self.driver.find_element(By.NAME, "save_safepay")

    def Get_PayNowSafePay__Element(self):
        "Returns the Element of PayNow Button of SafePay"
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def Get_CardNumber_Element(self):
        "Returns the Element of Card Number of MasterCard"
        return self.driver.find_element(By.ID,"creditCard")

    def Get_CVVNumber_Element(self):
        "Returns the Element of CVV Number of MasterCard"
        return self.driver.find_element(By.NAME,"cvv_number")

    def SendKeys_CVVNumber(self,CVV:int):
        self.Get_CVVNumber_Element().send_keys(f"1{CVV}")


    def Get_ExpirationDateMonth_Element(self):
        "Returns the Element of the Month Expiration Date of MasterCard"
        return self.driver.find_element(By.NAME,"mmListbox")

    def Select_ExpirationDateMonth(self,MonthNumber:int):
        "Chooses Month Number from Month Expiration Date dropdown list"
        MonthSelector = Select(self.Get_ExpirationDateMonth_Element())
        if(MonthNumber<10):
            MonthSelector.select_by_visible_text(f"0{MonthNumber}")
        else:
            MonthSelector.select_by_visible_text(f"{MonthNumber}")

    def Get_ExpirationDateYear_Element(self):
        "Returns the Element of the Year Expiration Date of MasterCard"
        return self.driver.find_element(By.NAME, "yyyyListbox")

    def Select_ExpirationDateYear(self,YearNumber:int):
        "Chooses Year Number from Year Expiration Date dropdown list"
        YearSelector = Select(self.Get_ExpirationDateYear_Element())
        YearSelector.select_by_visible_text(f"{YearNumber}")

    def Get_CardHolder_Element(self):
        "Returns the Element of The Card Holder of MasterCard"
        return self.driver.find_element(By.NAME, "cardholder_name")

    def Get_SaveChangedCheckBoxMasterCard_Element(self):
        "Returns the Element of SaveChanges CheckBox of MasterCard"
        return self.driver.find_element(By.NAME, "save_master_credit")

    def Get_PayNowMasterCard__Element(self):
        "Returns the Element of PayNow Button of SafePay"
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def Wait_ThankyouPageLoad(self):
        "Waits until thank you page loads"
        self.wait.until(EC.visibility_of_element_located((By.ID,"orderNumberLabel")))

    def Get_ThankYou_Element(self):
        "Returns The Element of the title of Thank you Page"
        return self.driver.find_element(By.CSS_SELECTOR,"#orderPaymentSuccess>h2>span")


    def Get_OrderNumber_Element(self):
        "Returns The Element of the order number from the thank you page"
        return self.driver.find_element(By.ID,"orderNumberLabel")

    def Get_TotalPrice_Element(self):
        "Returns The Element of the total cost of items without shipping from the thank you page"
        return self.driver.find_element(By.XPATH, "//div[@id='orderPaymentSuccess']/div/div[3]/div[1]/label/a")

    def TotalPriceDigits(self):
        "Returns Total price of items without shipping in Digits"
        return re.sub(r'[^0-9.]', '', self.Get_TotalPrice_Element().text)



