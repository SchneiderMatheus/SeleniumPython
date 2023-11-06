from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("textUsername").send_keys("Admin")
driver.find_element_by_id("textPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

act_title=driver.title
exp_title="OrangeHRM"
if act_title == exp_title:
    print("login Test Passed")
else:
    print("Login Test Failed")

driver.find_element_by_id("menu_pim_viewPimModule").click()
driver.find_element_by_id("firstName").send_keys("John")
driver.find_element_by_id("lastName").send_keys("Doe")
driver.find_element_by_id("btnSave").click()

select = Select(driver.find_element_by_id("jobTitle"))
select.select_by_value("1")

driver.find_element_by_id("radioButtonId").click()

alert = driver.switch_to.alert
alert.accept()

driver.execute_script("window.scrollBy(0, 300)")

driver.save_screenshot("screenshot.png")

driver.close()
