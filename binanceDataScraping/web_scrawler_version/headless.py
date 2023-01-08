# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:04:25 2022

@author: 22017
"""


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd
import os
from pathlib import Path
import shutil
import time


start_time = time.time()

# Creat a folder where we'll put the csv file
file_path = os.path.realpath(__file__)
path = Path(file_path).parent.absolute()
print('This file is in the folder : '+str(path))
file_path = os.path.realpath(__file__)
path = Path(file_path).parent.absolute()
path = str(path) + '\BinanceLeverageMargin'
print('The folder will be created here : ' + path)

# In case that the folder exists, delete the folder and creat a new one
if not os.path.exists(path):
    os.mkdir(path)
else:
    shutil.rmtree(path)
    os.mkdir(path)

# Webscraping launcher 
opt = Options()
opt.add_experimental_option('excludeSwitches', ['enable-automation'])

# Settings for headless driver
opt.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
print('Loading......')
driver.get("https://www.binance.com/en/futures/trading-rules/perpetual/leverage-margin")

#To wait until the element is attached
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-gnqbje")))

# To find the list of 'li' for symbols
sym_list = driver.find_elements(By.CSS_SELECTOR, ".css-1tsr9u1 .css-2rl2kr li")


# To create a list and put the 'title' of symboms into it
symbol_list = []
for s in sym_list:
    symbol_list.append(s.get_attribute('title'))

# Loop through symbol to webscrap the needed data and put them into csv files
for crypto in symbol_list:
    # To click on the search button 
    c = driver.find_element(By.CLASS_NAME, "css-z14ugq")
    driver.execute_script("arguments[0].click();", c)
    
    # To make sure the presence of the dropdown list  
    i = driver.find_element(By.CLASS_NAME, "css-1j7hzlq")
    driver.execute_script("arguments[0].click();", i)
    
    # To insert the 'title' of symbol in the box
    key = driver.find_element(By.CLASS_NAME, "css-vrydq2")
    key.send_keys(crypto)
    key.send_keys(Keys.RETURN)

    # To get the data table and headers for contracts
    table = driver.find_elements(By.CSS_SELECTOR, ".bn-table-row-level-0 .bn-table-cell")
    headers = driver.find_elements(By.CSS_SELECTOR, ".css-1f9551p .css-nxda0m")
    
    # To create a list of data
    data = []
    for t in table:
        data.append(t.text)
    
    # To creat a list of headers
    head = []
    for h in headers:
        head.append(h.text)
    
    # To creat 5 lists of data
    tier = []
    position_bracket = []
    max_leverage = []
    margin_rate = []
    maintenance_amount = []
    
    # Loop through and complete the five different lists 
    for i in range(len(data) // 5):
        tier.append(data[5 * i])
        position_bracket.append(data[5 * i + 1])
        max_leverage.append(data[5 * i + 2])
        margin_rate.append(data[5 * i + 3])
        maintenance_amount.append(data[5 * i + 4])
    
    # To create a dataframe
    d = {'Tier': tier, head[0]: position_bracket, head[1]: max_leverage,
         head[2]: margin_rate, head[3]: maintenance_amount}
    df = pd.DataFrame(d)
    name = crypto
    
    # To print data for each contract with the symbol name
    print(name)
    print(df)
    
    # To save the data as csv
    df.to_csv(path + '/{}.csv'.format(name), index=False)

# Record RunTime
print("This code ran sucessfully in", time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time)),"minutes.")


