from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\dell\Downloads\chromedriver_win32 (6)\chromedriver.exe")
driver.get("https://www.spicejet.com/")
driver.find_element_by_xpath("//div[@class='css-1dbjc4n r-zso239']").click()