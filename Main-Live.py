import os
import lxml
import smtplib
import dotenv
import requests
from bs4 import BeautifulSoup
dotenv.load_dotenv()
URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response=requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=header)
web=response
soup =BeautifulSoup(web.content,"html.parser")
alpha=soup.find(class_="a-offscreen").get_text()
#print(soup.prettify())
print(f"(   {alpha}  ) is the cost from the Amazon product")
bravo=soup.find(name='span', class_="a-size-large product-title-word-break",id="productTitle")
print(bravo.text)
print(f"The link is : {URL} ")
