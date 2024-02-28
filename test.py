import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.maximize_window()
# Opening JSON file
f = open('testData.json')
# returns JSON object as a dictionary
data = json.load(f)
# avoid duplication of data
unique = { each['name'] : each for each in data }.values()
unique = { each['age'] : each for each in data }.values()
unique = { each['gender'] : each for each in data }.values()
#convert dict to json
json_string = json.dumps(list(unique))

driver.find_element(By.XPATH,"//summary[normalize-space()='Table Data']").click()
driver.find_element(By.XPATH,"//textarea[@id='jsondata']").clear()
driver.find_element(By.XPATH,"//textarea[@id='jsondata']").send_keys(json_string)
driver.find_element(By.XPATH,"//button[@id='refreshtable']").click()

time.sleep(15)
# Closing file
f.close()
driver.quit()






