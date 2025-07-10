import os
import smtplib
import dotenv
import requests
from bs4 import BeautifulSoup
dotenv.load_dotenv()
URL='https://appbrewery.github.io/instant_pot/'

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response=requests.get(url='https://appbrewery.github.io/instant_pot/',headers=header)
web=response
soup =BeautifulSoup(web.content,"html.parser")

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 100

if price_as_float <BUY_PRICE:
    message = f"{title} as on sale for {price}"
    print(message)

    with smtplib.SMTP("smtp.gmail.com",port=587)as connection:
        connection.starttls()
        result=connection.login(os.environ["ENV_EMAIL"],os.environ["APP_CODE"])
        connection.sendmail(
            from_addr=os.environ["ENV_EMAIL"],
            to_addrs =os.environ["ENV_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
