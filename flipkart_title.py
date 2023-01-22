from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from IPython.display import Image, HTML
import pandas as pd
import time
import datetime
import numpy as np
import re
pd.set_option('display.max_columns', None)


driver_path = 'C:/Users/KARTHIKRAJ/Downloads/chromedriver_win32/chromedriver.exe'
input_path = 'amz_flip.csv'

def flipk_scrap(input_path,driver_path):
    df = pd.read_csv(input_path)
    df = df[df['result']==0]
    # print(df.head())
    flipk_pdp = df['flip_pdp_link'].to_list()
    flipk_given = df['given_flp_link'].to_list()
    all_list = list(zip(flipk_pdp,flipk_given))
    flipk_pdp_lst =[]
    link = []
    flipk_given_lst=[]
    title_lst =[]
        # df.to_csv('flip.csv')  
    driver =  webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()

    for i in all_list:
        # print(i)
        flipk_pdp_lst.append(i[0])
        flipk_given_lst.append(i[1])
        title_in =[]
        for link in i:
            flpk =link
            try:
                driver.get(flpk)
                try:    
                    title = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]').text
                    # print(title)
                    title_in.append(title)
                except:
                    title_in.append('NA')

            except:
                title_in.append('NA')
        title_lst.append(title_in)
    title_1 =[]
    title_2 =[]
    for j in title_lst:
        # print(j)
        title_1.append(j[0])
        title_2.append(j[1])
    dct ={'flipk_pdp_lst':flipk_pdp_lst,'flipk_given_lst':flipk_given_lst,'title_1':title_1,'title_2':title_2}
    final_df = pd.DataFrame(dct)
    final_df.to_csv('title_check.csv',index=False)
    return True


print(flipk_scrap(input_path,driver_path))