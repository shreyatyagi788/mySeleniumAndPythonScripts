from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
# time.sleep(2)

# driver.switch_to.alert.accept()
# time.sleep(2)

driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
# we can also use - driver.find_element(By.XPATH,"//text()='Click Me']").click()
time.sleep(2)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.dismiss()
time.sleep(2)

driver.close()
