from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
from selenium.webdriver.common.by import By
import time 
driver = wd.Firefox()
driver.get('https://www.dominos.ca')

Delivery = driver.find_element_by_css_selector('.btn.smart-order__cta.smart-order__cta--color')
Delivery.click()
time.sleep(1)

StreetAdd = driver.find_element_by_id('Street')
StreetAdd.send_keys('350 Victoria St')

City = driver.find_element_by_id('City')
City.send_keys('Toronto')

Region = Select(driver.find_element_by_id('Region'))
Region.select_by_visible_text('ON')

postal = driver.find_element_by_id('Postal_Code')
postal.send_keys('M5B 2K3')

con_Delivery = driver.find_element_by_css_selector('.btn.btn--large.btn--search-location.js-search-cta.c-locationsearch-search-cta')
con_Delivery.click()
time.sleep(3)

spec_Pizza = driver.find_element_by_id('entree-Pizza')
spec_Pizza.click()
time.sleep(2)

veg_Pizza = driver.find_element_by_css_selector('.media__image.productImage')
veg_Pizza.click()
time.sleep(2)
no_Custom = driver.find_element_by_css_selector('.btn.btn--large.js-isNew.js-addPizza.js-specialtyPizzaAdd.btn--speciality-add')
no_Custom.click()
time.sleep(2)
no_Cheese = driver.find_element_by_xpath('/html/body/div[24]/section/div/div[3]/div[3]/div[5]/div[3]/div/div/div/button[1]')
no_Cheese.click()

time.sleep(2)
checkout = driver.find_element_by_css_selector('.c-order-buttonCheckout-text')
checkout.click()
time.sleep(2)
close_Ad = driver.find_element_by_css_selector('.card--overlay__close.js-closeButton')
close_Ad.click()
time.sleep(2)
total = driver.find_element_by_css_selector('.finalizedTotal.js-total')
txt = total.get_attribute('innerText')
print("Total price is " + txt)
time.sleep(2)
final_checkout = driver.find_element_by_css_selector('.btn.btn--large.btn--block.btn--continue-checkout.submitButton.qa-OrCheck.js-continueCheckout.c-order-continueCheckout')
final_checkout.click()
time.sleep(4)
first_N = driver.find_element_by_id('First_Name')
first_N.send_keys('Sagar')

last_N = driver.find_element_by_id('Last_Name')
last_N.send_keys('PUNN')

email = driver.find_element_by_id('Email')
email.send_keys('example@yahoo.com')

phone = driver.find_element_by_id('Callback_Phone')
phone.send_keys('3333333333')

debit_Pay = driver.find_element_by_css_selector('.Delivery.is-hidden.c-order-payment-doordebit.js-paymentType')
debit_Pay.click()








class Order:
    def __init__(self, kind, address):
        self.kind = kind
        self.address = address
    def placeIt(keys):

"""



with open('keys.txt','r') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
print(lines)


def setupOrder(lines,address,fullname,email,phone):
    for line in lines:
        if line[0] == '.':
            elem = driver.find_element_by_css_selector(line)
            if line == '.finalizedTotal.js-total':
                print('Total Price of the order is " + elem.get_attribute('innerText'))
            else:
                elem.click()
        elif line[0] == '/':
            elem = driver.find_element_by_xpath(line)
            elem.click()
        else:
            elem = driver.find_element_by_id(line)
            if line == 'Street':
                (driver.find_element_by_id(line)).send_keys(address[0])
            elif line == 'City':
                (driver.find_element_by_id(line)).send_keys(address[1])
            elif line == 'Region':
                (driver.find_element_by_id(line)).select_by_visible_text(address[2])
            elif line == 'Postal_Code':
                (driver.find_element_by_id(line)).send_keys(address[3])
            elif line == 'entree-Pizza':
                (driver.find_element_by_id(line)).click()
            elif line == 'First_Name':
                (driver.find_element_by_id(line)).send_keys(fullname[0])
            elif line == 'Last_Name':
                (driver.find_element_by_id(line)).send_keys(fullname[1])
            elif line == 'Email':
                (driver.find_element_by_id(line)).send_keys(email)
            else:
                (driver.find_element_by_id(line)).send_keys(phone)
        time.sleep(4)







