from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")
wait = WebDriverWait(driver, timeout=10)
wait.until(expected_conditions.visibility_of_element_located("id","first_name"))

class _visibility(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)
   
    def __call__(self, driver):
        displayed = super().__call__(driver)
        if isinstance(displayed,WebElement):
            return displayed.is_enabled()
        else:
            return False
