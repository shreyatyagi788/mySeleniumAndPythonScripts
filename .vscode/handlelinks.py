from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests as requests
import time


serv_obj = Service("C:\\Users\\Aaryan\\Downloads\\shreyapythonfiles\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10) #the implicit wait is applicable to all ther statements in the script

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# perform click on the link.
driver.find_element(By.LINK_TEXT,"Comparison Table.").click()
driver.back()
time.sleep(5)

#find total number of links in a webpage.
totallinks = driver.find_elements(By.TAG_NAME,"a")
print("total number of links are", len(totallinks))

#print all the links.
for link in totallinks:
    print(link.text)

#identify total no of broken links without clicking on them with the help of 'requests' module.
count = 0
for link in totallinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    
    if res.status_code>=400:
        print(url, "is broken link")
        count+=1
    else:
        print(url, "is valid link")

print("total no. of broken links are:", count)