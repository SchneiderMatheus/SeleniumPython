from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\mathe\Downloads\chromedriver_win32 (1)\chromedriver")

driver = webdriver.ChromiumDriver(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
#("submit").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("login Test Passed")
else:
    print("Login Test Failed")

driver.close()
