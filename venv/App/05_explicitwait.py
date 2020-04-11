from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")

time.sleep(5)
driver.find_element_by_id("tab-flight-tab-hp").click()
#driver.find_element(By.ID, "tab-flight-tab-hp").click()
time.sleep(5)

driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("05/01/2020")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("05/01/2020")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Solve synchronization problem
# explicit wait is applicable for a particular elements of webpage
# Depends on condition instead of Time

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))

element.click()

time.sleep(5)
driver.quit()