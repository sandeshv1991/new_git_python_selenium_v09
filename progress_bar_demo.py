from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver-103.exe")
driver.get("file:///C:/Users/dell/OneDrive/Desktop/selnium_html_for%20practice/demo-html/progressbar.html")
driver.find_element_by_xpath("//button[text()='Click Me']").click()
wait=WebDriverWait(driver, timeout=3)
wait.until(expected_conditions.visibility_of_element_located(("xpath","//div[text()='100%']")))