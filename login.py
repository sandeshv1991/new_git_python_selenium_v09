from time import sleep
from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element_by_xpath("//a[@class='ico-login']").click()
driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("sandesh.venkatadri1991@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("Abcd@1234")
driver.find_element_by_xpath("//input[@value='Log in']").click()