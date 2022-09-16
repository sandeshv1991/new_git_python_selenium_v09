from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get("https://www.goibibo.com/")
driver.maximize_window()

driver.find_element_by_xpath("//span[contains(@class,'fswDownArrow')]").click()


for i in range(0,12):
    driver.find_element_by_xpath("//span[contains(@class,'--next')]").click()
    if ele in i:
        driver.find_element_by_xpath("//div[@aria-label='Sun Dec 04 2022']").click()
    
    
