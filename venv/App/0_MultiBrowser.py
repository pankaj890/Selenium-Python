from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create Driver Object
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")  # Chrome
#driver = webdriver.Chrome(executable_path="C:\Drivers\geckodriver.exe")   # Firefox

#driver.get("http://newtours.demoaut.com/")
driver.get("http://www.geminisolutions.com/solutions/technologies/backend-engineering/?tabid=1")

print(driver.title)     # Title of the Webpage
print(driver.current_url)     # URL of the Webpage
print(driver.page_source)     # HTML of the Webpage

driver.close()       # Close the browser - One window only