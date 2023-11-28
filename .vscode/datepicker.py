from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all the statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

date = "7"
month = "March"
year = "1997"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yy = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yy == year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

dates = driver.find_elements(By.XPATH,"//table[@class = 'ui-datepicker-calendar']//tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break

time.sleep(5)
driver.close()
