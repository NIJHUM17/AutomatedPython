
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

first_name = "Tahsin"
last_name = "Adiba"
email = "tahsinanijum5199@gmail.com"
password = "123Tahsin"

driver = webdriver.Chrome(service=Service('D:\Python\pythonProject\BasicSelenium\drivers\chromedriver.exe'))
driver.get("https://demo.opencart.com")
print(driver.title)

driver.find_element("xpath", "//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a/span").click()
time.sleep(3)
driver.find_element("xpath", "//*[@id='top']/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a").click()
time.sleep(3)
element = driver.find_element("id", "input-firstname")
element.send_keys(first_name)

element = driver.find_element("id", "input-lastname")
element.send_keys(last_name)

element = driver.find_element("id", "input-email")
element.send_keys(email)

element = driver.find_element("id", "input-password")
element.send_keys(password)

driver.find_element("xpath", "//*[@id='input-newsletter-yes']").click()
time.sleep(1)
driver.find_element("xpath", "//*[@id='form-register']/div/div/div/input").click()
time.sleep(1)

driver.close()
driver.quit()



