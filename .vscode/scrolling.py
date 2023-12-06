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

#1.scroll down page by pixel value.

# driver.execute_script("window.scrollBy(0, 1500)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("no. of pixels moved:",value)
# time.sleep(5)
# driver.close()

#2.scroll down the page untill specific element is visible.

# ele = driver.find_element(By.XPATH,"//div[@id='resizable']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# val = driver.execute_script("return window.pageYOffset;")
# print("no. of pixels moved:", val)
# time.sleep(5)
# driver.close()

#3.scroll down till the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
val = driver.execute_script("return window.pageYOffset;")
print("no. of pixels moved:",val)
time.sleep(5)
# driver.close()

#3.scroll up to startting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
val = driver.execute_script("return window.pageYOffset;")
print("no. of pixels moved:",val)
time.sleep(5)
driver.close()

