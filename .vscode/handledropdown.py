from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#select 'Norway' country from the dropdown.
#dpcountry = Select(driver.find_element(By.XPATH,"//select[@class = 'custom-select']"))
dpcountry = driver.find_elements(By.XPATH,"//select[@class = 'custom-select']/option")

#dpcountry.select_by_visible_text("Norway")
#time.sleep(5)

#print total no of options of the dropdown
#alloptions = dpcountry.options
print("total no of options are:", len(dpcountry))

#print all the options
for opt in dpcountry:
    print(opt.text)