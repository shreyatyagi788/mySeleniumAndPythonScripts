from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()

#driver.find_element(By.ID, "id-search-field").send_keys("python 3.7")
driver.find_element(By.NAME, "q").send_keys("python 3.7")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "search-button").click()
#driver.find_element(By.TAG_NAME, "button")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "About").click()
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "loads").click()
time.sleep(5)

"""Examples of customized locators
1 CSS Selector
2 XPATH."""

#driver.find_element(By.CSS_SELECTOR, "img.python-logo").click()
driver.find_element(By.CSS_SELECTOR, ".python-logo").click() #css selector with combination of tag and class.
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR, "input#id-search-field").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "#id-search-field").send_keys("selenium") #css selector with combination of tag and id.
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR, "a[rel=noopener]").click()
driver.find_element(By.CSS_SELECTOR, "[rel=noopener]").click() #css selector with combination of tag and any other attribute i.e other than id and class.
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR, "img.python-logo[alt='python™']").click() #css selector with combination of tag,class
#and any other attribute i.e other than id and class.
driver.find_element(By.CSS_SELECTOR, "a.action-trigger[xpath='1']")
#driver.find_element(By.CSS_SELECTOR, ".python-logo[alt='python™']").click()
time.sleep(5)



