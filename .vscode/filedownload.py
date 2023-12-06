from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
    # opt = webdriver.ChromeOptions()
    # opt.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-images-download/sample-png-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)
driver.close()


