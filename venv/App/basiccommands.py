from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

# Click on a Button
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close() # Colse only one Tab
driver.quit()   # Close the whole browser