from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd

# Connect to website
URL = 'https://www.amazon.in/Designer-Unicorn-Engineer-Because-Official/dp/B08JFBP1ZF/ref=pd_rhf_dp_s_pop_multi_srecs_sabr_4/262-0019943-4855247?pd_rd_w=0rikd&pf_rd_p=217ae98b-13ca-4bb5-a513-ddb3654ce36a&pf_rd_r=17NNRFYFRZSFJJCJJRE5&pd_rd_r=49606991-8cf9-4c3a-a949-3ddce94bd2fd&pd_rd_wg=ZSr8v&pd_rd_i=B08JFBP1ZF&psc=1'

# header from url:- httpbin.org/get
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

# Extracting data from Website reading HTML
page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text()
price = soup2.find(id='priceblock_ourprice').get_text()
rating = soup2.find(id='acrPopover').get_text()

# Printing data as per the requirements
title = title.strip()[0:]
print("Title = " + title)
price = price.strip()[1:]
print("Price = " + price)
rating = rating.strip()[0:]
print("Rating = " + rating)


today = datetime.date.today()
print(today)

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('Amazon_Scrapper_Dataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# Now appending data to the csv
with open('Amazon_Scrapper_Dataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

df = pd.read_csv(
    'D:\Git_Repo_My_Learnings\Amazon_Web_Scraping Using Python\Amazon_Scrapper_Dataset.csv')
print(df)


def check_price():

    # Connect to website
    URL = 'https://www.amazon.in/Designer-Unicorn-Engineer-Because-Official/dp/B08JFBP1ZF/ref=pd_rhf_dp_s_pop_multi_srecs_sabr_4/262-0019943-4855247?pd_rd_w=0rikd&pf_rd_p=217ae98b-13ca-4bb5-a513-ddb3654ce36a&pf_rd_r=17NNRFYFRZSFJJCJJRE5&pd_rd_r=49606991-8cf9-4c3a-a949-3ddce94bd2fd&pd_rd_wg=ZSr8v&pd_rd_i=B08JFBP1ZF&psc=1'

# header from url:- httpbin.org/get
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

# Extracting data from Website reading HTML
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id='priceblock_ourprice').get_text()
    rating = soup2.find(id='acrPopover').get_text()

    title = title.strip()[0:]
    print("Title = " + title)

    import datetime
    today = datetime.date.today()

    import csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('Amazon_Scrapper_Dataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    # if(price < 14):
    #     send_mail()


while(True):
    check_price()
    time.sleep(1)

# --In case use this code to snd email if price goes up or down
# def send_mail():
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login('mail_id', 'email_pwd')
#     subject = 'subject for the email'
#     body = 'matter for the email'
#     msg = f"Subject: {subject}\n\n{body}"
#     server.sendmail('emailid', msg)
