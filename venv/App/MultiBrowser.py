from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create Driver Object
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")  # Chrome
driver = webdriver.Chrome(executable_path="C:\Drivers\geckodriver.exe")   # Firefox

driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.close()       # Close the browser