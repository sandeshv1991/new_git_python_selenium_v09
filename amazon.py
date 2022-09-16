from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")

driver.get("https://www.amazon.com/")
driver.implicitly_wait(10)
driver.maximize_window()
a_obj = ActionChains(driver)

sign = driver.find_element_by_xpath("(//span[contains(@class,'-arrow')])[2]")

a_obj.move_to_element(sign).perform()

sleep(2)
driver.find_element_by_xpath("//span[text()='Account']").click()