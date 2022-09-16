from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver =  Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get(r"file:///C:/Users/dell/OneDrive/Desktop/selnium_html_for%20practice/demo-html/demo.html")

# price = driver.find_element_by_xpath("//td[text()='AAPL']/..//td[3]")
# print(price.text)


# details = driver.find_element_by_xpath("//td[text()='ALEX']/..//td[4]").text
# print(details)

elements = driver.find_elements_by_xpath("//table[@name='customers']//td[2]").text
print(elements)