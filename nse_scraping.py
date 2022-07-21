import selenium
from selenium import webdriver
import os
import time
import io
import pandas as pd
from selenium.common.exceptions import ElementClickInterceptedException

url='https://www.nseindia.com/market-data/top-gainers-loosers'
driver=webdriver.Firefox()
driver.get(url)
driver.maximize_window()

def scrap_data(x_path):
    share_info=driver.find_element_by_xpath(x_path)
    gainers=share_info.text
    line= gainers.split('\n')
    contents=[]
    for i in range(len(line)):
        line[i]=line[i].strip(',')
        contents.append(line[i].split(" "))
    columns=['SYMBOL','OPEN','HIGH','LOW','PREV.CLOSE','LTP','%CHNG','VOLUME','VALUE','CA']
    df=pd.DataFrame(contents[5:], columns=columns)
    return df

top_gainers=scrap_data('//*[@id="topgainer-Table"]')
top_gainers.to_csv("nse_gainers.csv")
#print(top_gainers)
loser_button=driver.find_element_by_xpath('/html/body/div[9]/div/section/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/a[2]')
loser_button.click()
top_losers=scrap_data('//*[@id="toplosers-Table"]')
top_losers.to_csv("nse_losers.csv")

driver.__exit__