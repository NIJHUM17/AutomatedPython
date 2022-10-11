from selenium import webdriver
from selenium.webdriver.chrome.service import Service
'''first_name = "Tahsin Adiba"
last_name = "Nijhum"
email = "tahsinanijum5199@gmail.com"
password = "123Tahsin"'''

#url = "http://automationpractice.com/index.php

pathdriver = Service("C:\Users\USER\Downloads\Path\chromedriver.exe")
driver = webdriver.Chrome(service=pathdriver)
driver.get("http://automationpractice.com/index.php")

driver.find_element().click()
driver.find_element().click()
time.sleep(3)

element = driver.find_element("")
element.send_keys(first_name)

element = driver.find_element("")
element.send_keys(last_name)






