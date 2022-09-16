from time import sleep
from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get("https://www.python.org/")
driver.maximize_window()
sleep(2)

links = driver.find_elements_by_xpath("//a")

# for link in links:
#     print(link.text,len(links))

# for link in links:
#     link_text=link.text
#     if "Python" in link_text:
#         print(link_text)

# for link in links:
#     print(link.get_attribute("href"))

url=[]
for link in links:
    link_text=link.text
    if "Python" in link_text:
        url.append((link_text,link.get_attribute("href")))
print(url)