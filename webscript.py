from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = wd.Firefox()
driver.get('https://www.dominos.ca')

#Reading css selectors and xpath from the file.
with open('keys.txt', 'r') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
print(lines)

f.close()

#Funtion that loops through the file lines and click/select accordingly 
def setupOrder(lines, address, fullname, email, phone):
    selected = False
    for line in lines:
        try:
            temp = (driver.find_element_by_css_selector(
                '.card--overlay__close.js-closeButton'))
            if(selected):
                temp.click()
            else:
                pass
            time.sleep(3)
        except:
            pass
        if line[0] == '.':
            try:
                elem = driver.find_element_by_css_selector(line)
                if line == '.finalizedTotal.js-total':
                    print('\nTotal Price of the order is' +
                          elem.get_attribute('innerText')+'\n')
                elif line == 'p.detailItem:nth-child(2) > strong:nth-child(2)':
                    print('\nYour pizza will be ready to be picked up at ' +
                          elem.get_attribute('innerText')+'\n')
                elif line == '.btn--no-thanks':
                    elem.click()
                    selected = True
                else:
                    elem.click()
            except:
                pass
            time.sleep(3)
        elif line[0] == '/':
            try:
                temp = (driver.find_element_by_xpath(line))
                temp.click()
                #print(line)
            except:
                #print('passed'+line)
                pass
            time.sleep(3)
        else:
            elem = driver.find_element_by_id(line)
            if line == 'Street':
                (driver.find_element_by_id(line)).send_keys(address[0])
            elif line == 'City':
                (driver.find_element_by_id(line)).send_keys(address[1])
            elif line == 'Region':
                (Select(driver.find_element_by_id(line))
                 ).select_by_value(address[2])
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
            time.sleep(1)


# Reading user information
address = []
fullN = []
address.append(input('\nEnter Street address:'))
address.append(input('\nEnter City:'))
address.append(input('\nEnter Province(Caps):'))
address.append(input('\nEnter Postal Code:'))
fullN.append(input('\nEnter First Name:'))
fullN.append(input('\nEnter Last Name:'))

phone = input('\nEnter phone number:')
email = input('\nEnter Email:')


# Finally passing user information to order funnction
print('\nSETTING UP THE ORDER\n')
setupOrder(lines, address, fullN, email, phone)


