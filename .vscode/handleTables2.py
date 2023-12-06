from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(20) #the implicit wait is applicable to all ther statements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("ADMIN")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
#driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
time.sleep(5)
act = ActionChains(driver)
ele = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")
act.click(ele).perform()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()
time.sleep(10)
rows = driver.find_elements(By.XPATH, "//div[@role='rowgroup']/div")
cols = driver.find_elements(By.XPATH,"//div[@role='rowgroup']/div[1]/div/div/div/div/div")
for col in cols:
    print(col.text)
driver.close()