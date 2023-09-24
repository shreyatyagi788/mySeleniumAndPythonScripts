from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")

#select the 'sunday' checkbox
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'sunday':
        checkbox.click()

#unselect the selected checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(5)
driver.close()
