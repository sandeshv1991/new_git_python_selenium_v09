from time import sleep
from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get(r"C:\Users\dell\OneDrive\Desktop\selnium_html_for practice\demo-html\demo.html")
driver.maximize_window()
sleep(2)

checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
for item in checkboxes:
    item.click()
    sleep(1)

print("length of check box =", len(checkboxes))

links=driver.find_elements_by_xpath("//a")
print("length of links =", len(links))
for link in links:
    link_tex=link.text
    if "Python" in link_tex:
        print(link_tex)

radios=driver.find_elements_by_xpath("//input[@type='radio']")
print("length of radio buttons =", len(radios))


driver.get("")

elements=driver.find_elements_by_xpath("//input[@name='download']")
for element in elements:
    element.click()
    sleep(1)

for element in elements[::-1]:
    element.click()
    sleep(1)

fill_in_the_boxes=driver.find_elements_by_name("fname")
words=['apple','books','pens','grapes','blueberries','violet','coldplay','warm','temperature']
for box,word in zip(fill_in_the_boxes,words):
    box.send_keys(word)


