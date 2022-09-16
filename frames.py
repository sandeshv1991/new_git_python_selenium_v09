from selenium.webdriver import Chrome
from time import sleep


driver=Chrome(r"C:\Users\sande\Desktop\chromedriver.exe")
driver.get("http://www.maths.surrey.ac.uk/explore/nigelspages/frame2.htm")
driver.maximize_window()

driver.switch_to.frame(0)
sleep(2)
driver.find_element_by_xpath("//a[text()=' Background']").click()
sleep(2)
driver.switch_to.frame(1)

sleep(2)
driver.find_element_by_name("name").send_keys("ranjith")
# sw = driver.find_element_by_xpath("//frame[@src='htmlf.htm']")
# driver.switch_to.frame(sw)
# sleep(2)
# driver.find_element_by_link_text("Beginners Guide").click()
# sleep(2)

# sw2 = driver.find_element_by_xpath("//frame[@src='tags.htm']")
# driver.switch_to.frame(sw2)
# sleep(2)
# driver.find_element_by_link_text("TRY CODING").click()

# sw1 = driver.find_element_by_xpath("//frame[@src='message.htm']")
# driver.switch_to.frame(sw1)
# driver.find_element_by_name("name").send_keys("sandesh")
# sleep(2)

# driver.switch_to.frame(sw1)
# sleep(2)
# driver.find_element_by_link_text("HTML Tags").click()
