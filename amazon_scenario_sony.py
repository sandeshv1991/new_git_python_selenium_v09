from selenium.webdriver import Chrome

driver = Chrome(r"C:\Users\sande\OneDrive\Desktop\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.find_element_by_xpath("//a[text()=' Electronics ']").click()
driver.find_element_by_xpath("//span[text()='Fitness trackers & smartwatches']").click()

prices = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

price_list = [price.text for price in prices]
#print(price_list)
for ele in price_list:
    if int(ele[-3::])<500:
        print(ele)
    


