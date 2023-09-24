from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://www.facebook.com/")
driver.maximize_window()

emailbox = webwait.until(EC.presence_of_element_located((By.XPATH, "//input[@class = 'inputtext _55r1 _6luy']")))
emailbox.send_keys("abc@gmail.com")
time.sleep(5)
driver.close()
