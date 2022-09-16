from time import sleep
from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
driver.maximize_window()
driver.find_element_by_link_text("Register").click()
driver.find_element_by_id("gender-male").click
sleep(2)
driver.find_element_by_id("FirstName").send_keys("Sandesh")
driver.find_element_by_id("LastName").send_keys("venkatadri")
sleep(2)
driver.find_element_by_name("Email").send_keys("sandesh.venkatadri1991@gmail.com")
driver.find_element_by_name("Password").send_keys("Abcd@1234")
driver.find_element_by_name("ConfirmPassword").send_keys("Abcd@1234")
sleep(2)
driver.find_element_by_id("register-button").click()