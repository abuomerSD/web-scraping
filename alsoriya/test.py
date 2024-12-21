from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd

url = 'https://alsourayia.com/ar/%D9%85%D9%88%D9%83%D9%8A%D8%AA-%D9%85%D9%83%D8%A7%D8%AA%D8%A8-%D8%A7%D9%8A%D8%B2%D9%8A-%D9%84%D8%A7%D9%8A%D9%86-2673'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(4)
specifications = driver.find_elements(By.CSS_SELECTOR, '.odd')

print(len(specifications))

size = driver.find_element(By.CSS_SELECTOR, '#quickTab-specifications > div > div.table-wrapper > table > tbody > tr:nth-child(2) > td.spec-value').get_attribute('innerHTML')
role_type = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('innerHTML')
product_body = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('innerHTML')
role_weight = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('innerHTML')
number_of_roles = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('innerHTML')
# backing = driver.find_element(By.XPATH, '')
main_lower = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('innerHTML')
second_lower = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('innerHTML')
role_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[9]/td[2]').get_attribute('innerHTML')
total_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[10]/td[2]').get_attribute('innerHTML')

product = [size, role_type, product_body, role_weight, number_of_roles,  main_lower, second_lower, role_height, total_height]

print(product)

