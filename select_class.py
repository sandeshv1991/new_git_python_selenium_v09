from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver = Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")
box = driver.find_element_by_id("standard_cars")
s = Select(box)

all_options = s.options

items = []
# for item in all_options:
#     items.append(item.text)

# print(items)
# for index,item in enumerate(all_options):
#     items.append((index,item.text))
# print(items)

# for item in items:
#     s.select_by_visible_text(item)
#     sleep(1)

# s.select_by_visible_text("Mercedes")

# s.select_by_visible_text(items[-1])
# sleep(1)

# s.select_by_value("aud")

# s.select_by_index(2)

for item in items[::-1]:
    s.select_by_visible_text(item)
    sleep(1)


