# import libraries 

import csv
from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd


def check_price():

    # Connect to Website and pull in data
    URL = 'https://www.amazon.com/Carhartt-Signature-Sleeve-T-Shirt-Heather/dp/B01BXHJ1YY/ref=sr_1_10?crid=B5OZBTBUX643&keywords=men+tshirts+casual+written&qid=1670439292&sprefix=men+tshirts+casual+written%2Caps%2C329&sr=8-10'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content,'html.parser')

    
    # Clean up the data a little bit
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    #remove excess spacing
    price = price.strip()[1:]
    title = title.strip()

    #fetching product title with help of it's ID and class
    title = soup2.find(id = "productTitle").get_text()
    price = soup2.find(class_ = "a-offscreen").get_text()


    # Create a Timestamp for your output to track when data was collected
    today = datetime.date.today()


    #Defining csv file col names and row values
    header = ['Title', 'Price', 'Date']
    data = [title, price,today]


     #Create CSV and write headers and data into the file
    #appending data to the csv
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    df = pd.read_csv('D:\Python Programs\AmazonWebScraperDataset.csv')
    print(df)


while(True):
    check_price()
    
    # Runs check_price after a set time and inputs data into your CSV
    time.sleep(86400)