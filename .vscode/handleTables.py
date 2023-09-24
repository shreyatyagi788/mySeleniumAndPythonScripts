from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows = len(driver.find_elements(By.XPATH,"//table[@name = 'BookTable']//tr"))
noOfCol = len(driver.find_elements(By.XPATH,"//table[@name = 'BookTable']//tr/th"))
#logic to print all the rows and column data.
for i in range(2,noOfRows+1):
    for j in range(1,noOfCol+1):
        data = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
        print(data, end = '             ')
    print()
driver.close()