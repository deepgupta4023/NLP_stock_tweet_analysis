import selenium
from selenium import webdriver
import os
import time
import io
import pandas as pd
from selenium.common.exceptions import ElementClickInterceptedException


url='https://www.bseindia.com/markets.html'
driver=webdriver.Firefox()
driver.get(url)
driver.maximize_window()

def convert(element):
    f= element.text
    line=f.split('\n')
    line[0]= line[0].replace('Change %', 'Change%')
    contents=[]
    for i in range(len(line)):
        contents.append(line[i].split(" "))
    return contents

def process(file):
    
    df=pd.DataFrame(file)
    header= df.iloc[0]
    df= df[1:]
    df.columns=header
    return df

time.sleep(5)
top_10_shares_button=driver.find_element_by_xpath('//*[@id="idGainers"]')
top_10_shares_button.click()
gainer_info=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/table')
gain= convert(gainer_info)
gainer= process(gain)
gainer.to_csv("top10.csv")
time.sleep(5)
bottom_10_shares_button=driver.find_element_by_xpath('//*[@id="idLosers"]')
bottom_10_shares_button.click()
loser_info=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div/div[2]/table')

lose= convert(loser_info)
losers= process(lose)
losers.to_csv("bottom10.csv")



#bottom_10_shares_button=driver.find_element_by_xpath('//*[@id="idLosers"]')
#bottom_10_shares_button.click()
