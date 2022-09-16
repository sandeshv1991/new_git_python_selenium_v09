from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")

driver.find_element_by_xpath("//button[contains(@class,'_2doB4z')]").click()
driver.find_element_by_xpath("//div[text()='Electronics']").click()
actions = ActionChains(driver)
electronics = driver.find_element_by_xpath("//span[text()='Electronics']")
actions.move_to_element(electronics).perform()

driver.find_element_by_xpath("//a[text()='Samsung']").click()

products = driver.find_elements_by_xpath("//a[@class='s1Q9rs']")
product_list = [product.text for product in products]
print(product_list)

prices = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
price_list = [price.text for price in prices]
print(price_list)




