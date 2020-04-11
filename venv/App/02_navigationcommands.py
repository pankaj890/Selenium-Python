package App

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title)
time.sleep(5)

driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)

driver.close()