from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\sande\Desktop\chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Twitter").click()

handles = driver.window_handles
driver.switch_to.window(handles[1])
sleep(2)

driver.find_element_by_xpath("//input[@placeholder = 'Search Twitter']").send_keys("hello")
sleep(3)

driver.switch_to.window(handles[0])
sleep(2)

driver.find_element_by_link_text("Register").click()