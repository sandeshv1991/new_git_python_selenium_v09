from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver=Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")
driver.maximize_window()
sleep(3)

driver.find_element_by_id("delete").click()
sleep(1)

driver.switch_to.alert.accept()
sleep(1)
text_ele=driver.find_element_by_xpath("//label[text()='You clicked Ok!!!']")
print(text_ele.text)
#fileupload pop_up
driver.find_element_by_id("resume").send_keys(r"C:\Users\dell\OneDrive\Desktop\sample_practice_resume_for_file_uploadpopup - Copy.txt")

