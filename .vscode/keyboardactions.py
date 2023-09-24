from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field2 = driver.find_element(By.XPATH,"//input[@id='field2']")
field1.clear()
field1.send_keys("welcome...")
act = ActionChains(driver)

#to perform ctrl+a on field1.
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#to perform ctrl+c on field1
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#to perform tab to move to field2
act.send_keys(Keys.TAB).perform()
# time.sleep(5)
#field2.click()
#to paste the text in field2 
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(10)
driver.close()
