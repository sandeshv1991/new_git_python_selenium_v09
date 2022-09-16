from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver=Chrome(r"C:\Users\sande\Desktop\chromedriver.exe")
driver.get(r"D:\selenium_html_for practice\demo-html\iframe.html")
driver.maximize_window()

driver.switch_to.frame("frame1")
sleep(2)
driver.find_element_by_link_text("Register").click()

driver.switch_to.default_content()
driver.switch_to.frame("frame2")
sleep(2)
driver.find_element_by_id("search_form").send_keys("hello world")
