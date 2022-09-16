from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\sande\Desktop\chromedriver.exe")
driver.get("https://in.bookmyshow.com/")

driver.implicitly_wait(10)

driver.find_element_by_xpath("//span[text()='Bengaluru']").click()
sleep(3)
driver.find_element_by_xpath("//div[@class='sc-chbbiW fcsTnZ']").click()