from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

# Solve synchronization problem
# Implicit wait is applicable for all elements of webpage
# Completely based on time we mention to wait
driver.implicitly_wait(10)  # secods wait

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()

