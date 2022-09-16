from time import sleep
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get("https://www.facebook.com/")

driver.implicitly_wait(10)
driver.find_element_by_link_text("Create New Account").click()
driver.find_element_by_name("firstname").send_keys("Raju")
driver.find_element_by_name("lastname").send_keys("master")
driver.find_element_by_name("reg_email__").send_keys("sandesh.venkatadri1991@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("sandesh.venkatadri1991@gmail.com")
driver.find_element_by_name("reg_passwd__").send_keys("Rameses@123")

#using select class

day = driver.find_element_by_id("day")
s_day = Select(day)
s_day.select_by_visible_text("18")
sleep(1)

month =  driver.find_element_by_id("month")
s_month = Select(month)
s_month.select_by_visible_text("Jan")
sleep(1)

year = driver.find_element_by_id("year")
s_year = Select(year)
s_year.select_by_visible_text("1991")
sleep(2)

driver.find_element_by_xpath("//label[.='Male']").click()

