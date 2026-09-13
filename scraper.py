import datetime as dt
import smtplib
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver=webdriver.Chrome(options=chrome_options)
EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')
#product link
product_link='https://www.flipkart.com/hashtag-fitness-wall-mounting-chin-up-pull-up-bar/p/itm7cf8165415229?pid=BAAFCZG9HWTEAHJV&lid=LSTBAAFCZG9HWTEAHJVZTA7DW&marketplace=FLIPKART&q=pull+up+bar&store=qoc%2Facb%2Fbuq&srno=s_1_13&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=search-autosuggest&iid=38d55cee-f416-42b7-98c5-b1b712742260.BAAFCZG9HWTEAHJV.SEARCH&ppt=sp&ppn=sp&ssid=dnm0li5nsw0000001788955545779&qH=3e005c5dc75a5c66&ov_redirect=true&ov_redirect=true'
#xpath of the price element
xpath='//*[@id="slot-list-container"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div/div/div/div/div/a/div/div[3]/div/'
Run=True
def send_email(subject,message):
        connection=smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f'Subject:{subject}\n\n{message}'
                )
        connection.close()
try:
        driver.set_page_load_timeout(60)
        driver.get(product_link)
        price_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
                )
        today_price=float(price_element.text.replace('₹','').replace(',',''))
except Exception as e:
        send_email(f'Scraper failed','Unable to locate element.\nError:{e}')
        Run=False
if Run:
        try:
                history=pd.read_csv('output.csv')
                old_price=float(history['price'].iloc[-1])
        except (FileNotFoundError, pd.errors.EmptyDataError):
                old_price = None
        new_data={'date':dt.datetime.today().date(),'price':today_price}
        df=pd.DataFrame([new_data])
        df.to_csv('output.csv',header=not os.path.exists('output.csv'),mode='a',index=False)
        if old_price is not None and today_price<old_price:
                send_email('Price update',f'Hurry up!!\nThe price is changed from {old_price} to {today_price}.')

driver.quit()
graph_data=pd.read_csv('output.csv')
graph_data['date'] = pd.to_datetime(graph_data['date'])
plt.figure(figsize=(10,5))
plt.plot(graph_data['date'],graph_data['price'],marker='o')
plt.title('Price history')
plt.xlabel("Date")
plt.ylabel("Price (₹)")
plt.savefig("price_history.png")
plt.close()
