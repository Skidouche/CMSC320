from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

#create the driver
driver = webdriver.Chrome()
driver.get("https://pypl.github.io/PYPL.html")

#scrape the table body
tbody = driver.find_element(By.XPATH, '//*[@id="table"]/table/tbody')

#Loop through relevant columns and add to a matrix of langage, share, and trend by reading as html
data = [[], [], []]
for i in range(3, 6):
    for j in tbody.find_elements(By.XPATH, f'//*[@id="table"]/table/tbody/tr/td[{i}]'):
        data[i - 3].append(j.text)

#List all languages
for lang in data[0]:
    print(lang)
print(f"\n")

#List top five languages with relevant information
for i in range (0, len(data[0])):
        print (data[0][i] + " " + data[1][i] + " " + data[2][i])
    
        

#Report median share value of languages
for elem in data[1]:
    

#List highest languages by highest trend

driver.quit

