import requests
from bs4 import BeautifulSoup
import pandas as pd

#Configure the proxy
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080",
}

data = {'Title': [], 'Price': []}

url = "https://www.amazon.in/s?k=iphone&crid=3RI2304SBAXSA&sprefix=iphone%2Caps%2C105&ref=nb_sb_noss_2"

#Configure the header to bypass
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# spans = soup.find(class_="a-size-medium") # it will display all the details of the page
# print(spans)

# spans1 = soup.select("div.sg-col-inner") 
# print(spans1)
#  prices = soup.select("span.a-price")

#Fetch the title of each products
spans2 = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans2:  
    print(span.string)
    data["Title"].append(span.string)

#Fetch the price of each products
for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["Price"].append(price.find("span").get_text())
        if len(data["Price"]) == len(data["Title"]):
            break

# Write the data into excel
df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index=False)