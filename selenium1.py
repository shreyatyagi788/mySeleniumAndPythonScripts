from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome() #if drivers are installed in the same location where python is installed,
#then it will automatically get those drivers location we don't need to specify the path.
#driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.find_element(By.NAME, "username").send_keys("ADMIN")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("login test pass")
else:
    print("login test fail")
driver.close()