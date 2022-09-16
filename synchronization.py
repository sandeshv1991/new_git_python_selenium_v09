from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")
wait = WebDriverWait(driver, timeout=10)
wait.until(expected_conditions.visibility_of_all_elements_located(("name","fname")))
driver.find_element_by_name("fname").send_keys("Hello World")

