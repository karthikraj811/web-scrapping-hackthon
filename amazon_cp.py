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
pd.set_option('display.max_columns', None)


driver_path = 'C:/Users/KARTHIKRAJ/Downloads/chromedriver_win32/chromedriver.exe'
input_path = 'C:\Hackathon\hackathon_input_veirdo.csv'

def scrapper(driver_path, input_file):
    start=time.time()
    df= pd.read_csv(input_file) 
    list_url = df['Amazon_URL'].to_list()
    Product_ID=[]
    Title=[]
    Selling_Price=[]
    MRP=[]
    Category=[]
    Product_Detail=[]
    Product_URL=[]
    Seller_Name=[]
    Description=[]
    Style_Id=[]
    url =[]
    driver =  webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    for i in list_url:
    # for i in ['https://www.amazon.in/dp/B09XX9SB44']:
        web = i+'?th=1&psc=1'
        driver.get(web)
        Product_URL.append(web)
        prod_id=i
        Product_ID.append(prod_id)
        time.sleep(2)
        try:   
            title = driver.find_element(By.XPATH,"//span[@id='productTitle']").text
            Title.append(title)
        except:
            title = 'na'
            Title.append(title)
        time.sleep(2)

        try:    
            price = driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text 
            Selling_Price.append(price)
        except:
            price = 0
            Selling_Price.append(price)
        try:
            mrp = driver.find_element(By.XPATH,'//span[@class="a-price a-text-price"]').text
            MRP.append(mrp)
        except:
            mrp = ''
            MRP.append(mrp)
        try:    
            cate = driver.find_element(By.XPATH,'//div[@id="wayfinding-breadcrumbs_feature_div"]').text 
            Category.append(cate)
        except:
            cate = 'na'
            Category.append(cate)
        
        try:
            detail=driver.find_element(By.XPATH,'//div[@id="detailBullets_feature_div"]').text
            Product_Detail.append(detail)
        except:
            detail = 'na'
            Product_Detail.append(detail)
        

        try:
            seller=driver.find_element(By.XPATH,'//div[@id="merchant-info"]').text
            Seller_Name.append(seller)
        except:
            seller = 'na'
            Seller_Name.append(seller)
        try:
            description=driver.find_element(By.XPATH,'//div[@id="featurebullets_feature_div"]').text
            Description.append(description)
        except:
            description = 'na'
            Description.append(description)
        try:    
            style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[1]').text 
            if style_id == 'Item part number :':
                
                style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]').text
            else:
                style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span[1]').text
                if style_id == 'Item part number :':
                
                    style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span[2]').text
                else:
                    style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span[1]').text
                    if style_id == 'Item part number :':
                
                        style_id = driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span[2]').text
                    else:
                        style_id ='NA'
            Style_Id.append(style_id)


        except:
            Style_Id.append('0')
        url.append(i)


    end=time.time()
    print("Total time taken:{}seconds".format(round((end-start))))
    
    dct={'amz_url':url,'Title':Title, 
         'Category':Category, 'Selling Price':Selling_Price, 'MRP':MRP, 
         'Seller Name':Seller_Name, 'Product Details':Product_Detail,'Description':Description,'style_id':Style_Id}

    df1 = pd.DataFrame(dct)
    df1.to_csv('test2.csv')
    return 'Done'
    

print(scrapper(driver_path,input_path))



