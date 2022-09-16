from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver import Chrome
driver = Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()

# elements=driver.find_elements_by_xpath("//span[@class='price actual-price']")
# for element in elements:
#     print(element.text)

# elements=driver.find_elements_by_xpath("//a[text()='$25 Virtual Gift Card']/../..//span[@class='price actual-price']")
# for element in elements:
#     print(element.text)
products = driver.find_elements_by_xpath("//h2[@class='product-title']")
product_list=[product.text for product in products]
#print(product_list)
# for product in products:
#     print(product.text)

prices=driver.find_elements_by_xpath("//span[@class='price actual-price']")
price_list=[price.text for price in prices]
product_price={}
for product,price in zip(product_list,price_list):
    product_price[product]=float(price)
print(product_price)
