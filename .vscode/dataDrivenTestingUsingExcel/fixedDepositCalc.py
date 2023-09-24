from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import excelUtils
import time

serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all the statements or web elements in the script
#webwait = WebDriverWait(driver, 10, 2,ignored_exceptions=Exception) #explicit wait(we need to write explicit wait for particular element)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
file = "C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\caldata.xlsx"

rows = excelUtils.getRowCount(file,'Sheet1')
#getting excel data.
for r in range(2,rows+1):
    princ = excelUtils.getCellData(file,'Sheet1',r,1)
    ratOfInterest = excelUtils.getCellData(file,'Sheet1',r,2)
    per1 = excelUtils.getCellData(file,'Sheet1',r,3)
    per2 = excelUtils.getCellData(file,'Sheet1',r,4)
    freq = excelUtils.getCellData(file,'Sheet1',r,5)
    expMatVal = excelUtils.getCellData(file,'Sheet1',r,6)

    #filling the date to the website.
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ratOfInterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    driver.find_element(By.XPATH,"//select[@id='tenurePeriod']").send_keys(per2)
    freqele=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freqele.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//div[@class='CTR PT15']/a[1]/img[1]").click()

    actMatVal = driver.find_element(By.XPATH,"//span/strong").text

    if float(actMatVal) == float(expMatVal):
        print("test passed")
        excelUtils.writeCellData(file,'Sheet1',r,8,"passed")
        excelUtils.fillGreenColour(file,'Sheet1',r,8)
    else:
        print("test failed")
        excelUtils.writeCellData(file,'Sheet1',r,8,"passed")
        excelUtils.fillRedColour(file,'Sheet1',r,8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(2)
