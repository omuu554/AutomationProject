from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re



class OrderPaymentLogClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Get_SelectedDetails_Element(self):
        "Returns the Element of the selected Detailels(Shipping/Payment)"
        return self.driver.find_element(By.CSS_SELECTOR,"#detailslink>label.selected")

    def Wait_UntilOrderPaymentLogLoaded(self):
        self.wait.until(EC.element_to_be_clickable(self.Get_Next_Element()))

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

    def SendKeys_CVVNumber(self,CVV:str):
        "Sends Keys to CVV Number"
        self.Get_CVVNumber_Element().send_keys(f"{CVV}")

    def SendKeys_CVVNumberGlitch(self,CVV:str):
        "Fixes a glitch where CVV Number disapears when Sending Keys in automation"
        while(self.Get_CVVNumber_Element().get_attribute('value') != CVV):
            self.Get_CVVNumber_Element().clear()
            self.SendKeys_CVVNumber(CVV)


    def SendKeys_CardNumber(self,CardNumber:str):
         "Sends Keys to Card Number"
         self.Get_CardNumber_Element().send_keys(f"{CardNumber}")

    def SendKyes_CardNumberGlitch(self,CardNumber:str):
        "Fixes a glitch where Card Number disapears when Sending Keys in automation"
        while(self.Get_CardNumber_Element().text != CardNumber):
            self.Get_CardNumber_Element().clear()
            self.SendKeys_CardNumber(CardNumber)


    def Get_ExpirationDateMonth_Element(self):
        "Returns the Element of the Month Expiration Date of MasterCard"
        return self.driver.find_element(By.NAME,"mmListbox")

    def Select_ExpirationDateMonth(self,MonthNumber:int):
        "Chooses Month Number from Month Expiration Date dropdown list"
        MonthNumber = int(MonthNumber)
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
        YearNumber = int(YearNumber)
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

    def Get_PayNowMasterCardHidden_Element(self):
        return self.driver.find_element(By.ID, "pay_now_btn_MasterCredit")

    def Click_PayNowMasterCard(self):
        ActionChains(self.driver).move_to_element(self.Get_PayNowMasterCard__Element()).click().perform()

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
        return float(re.sub(r'[^0-9.]', '', self.Get_TotalPrice_Element().text))

    def Get_EditCard_Element(self):
        "Returns the element of edit Card button"
        return self.driver.find_element(By.CSS_SELECTOR, ".masterCreditSeccion>div>label")

    def IsEditCardDispalyed(self):
        "checkes wether the element of edit Card button is shown"
        return self.Get_EditCard_Element().is_displayed()

    def Click_EditCard(self):
        "Click on edit Card button if its is shown"
        if(self.IsEditCardDispalyed()):
            self.Get_EditCard_Element().click()




