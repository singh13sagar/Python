from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

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
elem3.send_keys("hello")


print(driver.current_url)
driver.close
