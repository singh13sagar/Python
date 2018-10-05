from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time 



driver = wd.Firefox()

driver.get('https://www.dominos.ca')

assert 'Domino\'s' in driver.title

#driver.findElement(by.className('btn btn--delivery js-delivery')).click()
elem = driver.find_element_by_xpath('/html/body/header/nav/div[3]/ul/li[1]/a')
print(elem)
elem.click()
print(driver.current_url)
#elem.clear()
#elem.send_keys('pycon')
#elem.send_keys(Keys.RETURN)

assert 'No results found.' not in driver.page_source
elem2 =  driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/form/div/div[1]/div[2]/div[1]/div/label[1]/span[1]')
print(elem2)
elem2.click()

time.sleep(2)

elem3 =  driver.find_element_by_xpath('//*[@id="Street"]')
elem3.send_keys("Victoria St")

elem4 =  driver.find_element_by_xpath('//*[@id="Address_Line_2"]')
elem4.send_keys("350")

elem5 =  driver.find_element_by_xpath('//*[@id="City"]')
elem5.send_keys("Toronto")

elem6 =  driver.find_element_by_xpath('//*[@id="Postal_Code"]')
elem6.send_keys("M5B 2K3")


select = Select(driver.find_element_by_xpath('//*[@id="Region"]'))
select.select_by_visible_text('ON')

time.sleep(2)

elem7 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/form/div/div[2]/div/button')
print(elem7)
elem7.click()
print(driver.current_url)



print(driver.current_url)
driver.close
