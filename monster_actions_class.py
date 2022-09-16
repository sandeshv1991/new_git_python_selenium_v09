from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\dell\OneDrive\Desktop\chromedriver.exe")
driver.get("https://www.monsterindia.com/")
sleep(3)

actions = ActionChains(driver)

job_search = driver.find_element("xpath","//a[text()='Job search']")
actions.move_to_element(job_search).perform()
sleep(2)

job_by_skill = driver.find_element("xpath","//a[text()='Jobs by Skills']")
actions.move_to_element(job_by_skill).perform()
sleep(2)

python_jobs = driver.find_element("xpath", "//a[contains(text(),'Python Jobs')]")
actions.move_to_element(python_jobs).perform()
sleep(2)

python_jobs.click()
