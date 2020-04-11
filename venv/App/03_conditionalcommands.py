from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

# Check status of any field on wbpage
user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

# Populate values in the fields and login
user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

# Radio Buttons
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())

oneway_radio = driver.find_element_by_css_selector("input[value=oneway]")
print(oneway_radio.is_selected())

time.sleep(10)
driver.close()