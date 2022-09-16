from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")

list_box = driver.find_element_by_id("multiple_cars")
s = Select(list_box)
s.select_by_visible_text("BMW")
sleep(1)
s.select_by_value("aud")
sleep(1)
s.select_by_index(2)
sleep(3)

s.deselect_by_index(2)
sleep(1)
s.deselect_by_value("aud")
sleep(1)
s.deselect_by_visible_text("BMW")



