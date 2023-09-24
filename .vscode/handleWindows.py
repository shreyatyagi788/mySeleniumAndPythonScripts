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

driver.find_element(By.XPATH,"//input[@id = 'Wikipedia1_wikipedia-search-input']").send_keys("selenium")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']/div/child::a")
for result in results:
    result.click()
time.sleep(5)
windowIds = driver.window_handles
for id in windowIds:
    driver.switch_to.window(id)
    print(driver.title)
time.sleep(5)
driver.quit
()

