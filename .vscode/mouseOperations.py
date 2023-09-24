from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1. double click mouse action

# field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
# field1.clear()
# field1.send_keys("welcome...")
# button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# act = ActionChains(driver)
# act.double_click(button).perform()
# time.sleep(5)
# driver.close()

#2. drag and drop mouse action

# source = driver.find_element(By.XPATH, "//div[@id='draggable']")
# dest = driver.find_element(By.XPATH, "//div[@id='droppable']")
# act = ActionChains(driver)
# act.drag_and_drop(source,dest).perform()
# time.sleep(5)
# driver.close()

#3. moving slider mouse action

slider = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print("location of slider before moving:",slider.location)
act = ActionChains(driver)
act.drag_and_drop_by_offset(slider,100,0).perform()
print("location of slider after moving:",slider.location)
time.sleep(5)
driver.close()

