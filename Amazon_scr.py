# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:21:45 2022

@author: User
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from IPython.display import Image, HTML
import pandas as pd
import numpy as np
import time
from datetime import datetime
from selenium.webdriver.firefox.options import Options
import random



driver_path = 'C:/Users/KARTHIKRAJ/Downloads/chromedriver_win32/chromedriver.exe'
input_path = 'C:\Hackathon\hackathon_input_veirdo.csv'



def scrapper(input_file,driver_path):

    inp=pd.read_csv(input_file)
    list_url = inp['Amazon_URL'].to_list()
    Title = list()
    Price = list()
    Color = list()
    Style_Id = list()
    Mrp= list()
    Material= list()
    Style= list()
    Neck_style= list()
    Description= list()
    Department= list()
    Manufacture= list()

    code = []
    # xp=dict(zip(xp['KPI'],xp['XPATH']))
    # for amz_url in list_url[:5]:
    for amz_url in ['https://www.amazon.in/dp/B09XX9SB44']:
        # Create a new Chrome driver with the desired capabilities
        driver =  webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()
        web = amz_url
        driver.get(web)
        print(amz_url)
        try:
            driver.find_element(By.ID,'size_name_0').click()
            time.sleep(1)    
        except:
            pass
        try:
            title = driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
            Title.append(title)
        except:
            title = 'nan'
            Title.append(title)
            time.sleep(1)
        try:    
            price = driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text 
            Price.append(price)
        except:
            Price.append('0')
            time.sleep(1)
        try:    
            mrp = driver.find_element(By.XPATH,".//span[contains(@class,'a-price a-text-price') and contains(@data-a-size,'b')]").text 
            Mrp.append(mrp)
        except:
            Mrp.append('0')
            time.sleep(1)
        try:    
            color = driver.find_element(By.XPATH,'//*[@id="inline-twister-expanded-dimension-text-color_name"]').text 
            Color.append(color)
        except:
            Color.append('0')
            time.sleep(1)
        try:    
            material = driver.find_element(By.XPATH,'//*[@id="productFactsDesktopExpander"]/div[1]/div[1]/div/div[2]/span').text 
            Material.append(material)
            
        except:
            Material.append('0')
            time.sleep(1)

        try:    
            style = driver.find_element(By.XPATH,'//*[@id="productFactsDesktopExpander"]/div[1]/div[2]/div/div[2]/span').text 
            Style.append(style)
        except:
            Style.append('0')
            time.sleep(1)

        try:    
            neck_style = driver.find_element(By.XPATH,' //*[@id="productFactsDesktopExpander"]/div[1]/div[3]/div/div[2]/span').text 
            Neck_style.append(neck_style)
        except:
            Neck_style.append('0')
            time.sleep(1)

        try:    
            description = driver.find_element(By.XPATH,'//*[@id="productFactsDesktopExpander"]/div[1]/ul[4]/li/span').text 
            Description.append(description)
        except:
            Description.append('0')
            time.sleep(1)

        try:    
            department = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[7]/span/span[2]').text 
            Department.append(department)
        except:
            Department.append('0')
            time.sleep(1)

        try:    
            manufacture = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[8]/span/span[2]').text 
            Manufacture.append(description)
        except:
            Manufacture.append('0')
            time.sleep(1)
        try:    
            style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]').text 
            Style_Id.append(style_id)
        except:
            Style_Id.append('0')
            time.sleep(1)
        code.append(amz_url)
        driver.close()
    merge_list = list(zip(Title,Price,Mrp,Color,Material,Style,Neck_style,Description,Department,Manufacture,Style_Id))
    merg_df = pd.DataFrame(merge_list,columns=['Title','Price','Mrp','Color','Material','Style','Neck_style','Description','Department','Manufacture','Style_Id'])
    merg_df.to_csv('test_scr.csv',index=False)
    

    #         try:
    #             driver.find_element(By.ID,xp['click']).click()
    #             time.sleep(1)    
    #             driver.find_element(By.XPATH,xp['send_keys']).send_keys(i)
    #             driver.find_element(By.XPATH, xp['click2']).click()
    #             time.sleep(1)
    #         except:
    #             pass

    #         try:
    #             now = datetime.now()
    #             date_time1 = now.strftime("%d/%m/%Y %H:%M:%S")
    #             Date.append(date_time1)
    #             week=now.strftime("%V")
    #             Week.append(week)
    #             channel='Amazon'
    #             Marketplace.append(channel)
    #             Product_id.append(j)
    #         except:
    #             pass
    #         try:
    #             title = driver.find_element(By.XPATH,xp['title']).text
    #             Title.append(title)
    #         except:
    #             title = 'nan'
    #             Title.append(title)
    #         time.sleep(1)

    #         try:    
    #             price = driver.find_element(By.XPATH,xp['price']).text 
    #             Price.append(price)
    #         except:
    #             Price.append('0')
    #         try:    
    #             discount = driver.find_element(By.XPATH,'//span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"]').text
    #             Discount.append(discount) 
    #         except:
    #             discount = 0
    #             Discount.append(discount)
    #         try:
    #             mrp = driver.find_element(By.XPATH,'//span[@class="a-price a-text-price"]').text
    #             MRP.append(mrp)
    #         except:
    #             mrp = ''
    #             MRP.append(mrp)
    #         try:

    #             d=driver.find_element(By.XPATH,xp['delivery']).text 
    #             delivery.append(d)

    #         except:
    #             delivery.append('NaN')
    #         time.sleep(1)    
    #         driver.close()

    #     print(len(Price),len(Title),len(delivery),len(code),len(Product_id),len(Marketplace),len(Date),len(Week))

    #     data=pd.DataFrame({'Title':Title,'Week':Week,'Date':Date,'Marketplace':Marketplace,'Product ID':Product_id,
    #                        'Pincode':code,'Selling Price':Price,'MRP':MRP,'Discount':Discount,'Estimated Delivery Date':delivery})



    #     data['Brand'] = data['Title'].str.split(' ').str[0:2].apply(lambda x:" ".join(x))
    #     data['Date'] = pd.to_datetime(data.Date, format='%d/%m/%Y %H:%M:%S')
    #     a=[str(i) for i in data['Estimated Delivery Date']]
    #     b=[]
    #     for i in a:
    #         if len(i)<5:
    #             b.append('No')
    #         else:
    #             b.append('Yes')

    #     data['In Stock']=pd.Series(b)
    #     data['Selling Price']=data['Selling Price'].replace('','0')
    #     data['Selling Price']=data['Selling Price'].str.replace('.','')
    #     data['Selling Price']=data['Selling Price'].astype(int)
    #     data['Estimated Delivery Date']=data['Estimated Delivery Date'].str.split(' ').str[3:5].apply(lambda x:" ".join(x))
    #     data['Estimated Delivery Date']=data['Estimated Delivery Date'].str.replace('.','')
    #     data['Week']=data['Week'].astype(int)
    #     data['Pincode']=data['Pincode'].astype(str)
    #     # MRP processing
    #     mrp_li = list(data['MRP'])
    #     mrp_out = []
    #     for i in mrp_li:
    #         try:
    #             mrp_out.append(int(float(''.join(i.strip('₹').split(',')))))
    #         except:
    #             mrp_out.append(0)

    #     data['MRP'] = mrp_out
    #     data['Discount']= data['Discount'].str.findall(r'(\d)').str.join('')
    #     data['Discount']= data['Discount'].replace(np.nan,0)
    #     data['Discount']=data['Discount'].astype(int)
    #     data=data[['Date','Week','Marketplace','Product ID','Pincode','Brand','Title','Selling Price','MRP','Discount','Estimated Delivery Date','In Stock']]
    # return data


print(scrapper(input_path,driver_path))