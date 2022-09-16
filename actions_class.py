from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
# driver.get("https://www.monsterindia.com/")
# driver.maximize_window()

# a_obj=ActionChains(driver)
# ele=driver.find_element_by_xpath("//a[.='Job search']")
# a_obj.move_to_element(ele).perform()
driver.get(r"file:///C:/Users/dell/OneDrive/Desktop/selnium_html_for%20practice/demo-html/demo.html")
driver.maximize_window()

a1_obj = ActionChains(driver)
double = driver.find_element_by_xpath("//button[text()='Double-click me']")
a1_obj.double_click(double).perform()
texter = driver.find_element_by_id("double-click-message").text
print(texter)


