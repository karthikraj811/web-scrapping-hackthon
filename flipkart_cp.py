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
input_path = 'C:\Hackathon\hackathon_input_veirdo.csv'

def flipk_scrap(input_path,driver_path):
    df = pd.read_csv('test2.csv')
    df = df[(df['style_id']!='NA') & (df['style_id']!='0') & (df['style_id']!='Yellow co-ords')]
    df['brand'] = df['Title'].apply(lambda x:'veirdo' if 'veirdo' in x.lower() else 'juneberry')
    brand_lst = df['brand'].to_list()
    style_lst = df['style_id'].to_list()
    amz_lst = df['amz_url'].to_list()
    all_list = list(zip(brand_lst,style_lst,amz_lst))
    flip_url_lst =[]
    link = []
    style_id_lis=[]
    amz_url_list =[]
    # df.to_csv('flip.csv')  
    driver =  webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()

    for i in all_list:
        # new_style_id = i[1].split('_')
        # len_stl_id = len(new_style_id)
        # if len(new_style_id)> 2:
        #     new_style_id = "_".join(new_style_id[:len_stl_id-1])
        # elif len_stl_id == 2:
        #     new_style_id = "_".join(new_style_id)
        # else:
        #    new_style_id = new_style_id[0]
        # print(new_style_id)
            
        flip_url = 'https://www.flipkart.com/search?q='+i[0]+'%20'+i[1]
        driver.get(flip_url)
        flip_url_lst.append(flip_url)
        style_id_lis.append(i[1])
        amz_url_list.append(i[2])
        time.sleep(2)
        try:    
            price = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div').get_attribute('data-id')
            # price = re.findall('pid*&?',price)
            print('\n')
            print(price)
            link_p = 'https://www.flipkart.com/x/p/k?pid='+price
            link.append(link_p)
        except:
            link.append('NA')
    
    dct ={'amz_url':amz_url_list,'style_id':style_id_lis,'flip_url':flip_url_lst,'flip_pdp_link':link}
    final_df = pd.DataFrame(dct)
    final_df.to_csv('amz_flip1.csv',index=False)
    return True


print(flipk_scrap(input_path,driver_path))