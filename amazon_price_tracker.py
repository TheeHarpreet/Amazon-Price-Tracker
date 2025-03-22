import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import pandas as pd
from twilio.rest import Client
import sys

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

amazon_urls = [
    "https://www.amazon.co.uk/HyperX-Cloud-III-Wireless-microphone/dp/B0CBQXGZ85/ref=sr_1_3?crid=3O4L7FIW1G5WP&dib=eyJ2IjoiMSJ9.3yYeaH1TffjXsqz_Omeyd8MPlzq1rIoFC62eyC-7V_MqRzOQluZLokyuGxVtJnxvcoq6kyUY4nz1cwVQsKPDnP4EICL4sRC7d5yQKTmJ2LQ_zamUTPNUfNMVnmOsTZqsyv6FxwA3esZqwdftoUPIc8jVk_q6Z74uSnjhv9ZreIzakN9XUQdFPddS88Pp_8NtgSOsX5Jl35P07mzJW0Bww5WItmtOja3bBZchLoHzHeo.-FekELGkILAJURoUTK4U9mvR9Kf5XEgRJfRPBWc5Z5E&dib_tag=se&keywords=cloud%2B3%2Bwireless&qid=1742561073&sprefix=cloud%2B3%2Bwireless%2Caps%2C84&sr=8-3&ufe=app_do%3Aamzn1.fos.9c21b5d8-763b-46f5-a19a-62aef163feca&th=1",
    "https://www.amazon.co.uk/Beauty-of-Joseon-Relief-Sun/dp/B09JVNZVH3/ref=sr_1_5_pp?crid=JHSHPMASWSCT&dib=eyJ2IjoiMSJ9.Z9Cqow73IXkp-_ODyhSN4Cy5X5pMYvbGA2yBPJvx_qziilyVtB78zttzByvaAaZBMfKIkgughyOFFPITuSrsUtul-I9kcmwbovEQESEwnzGGhkZ6jMzmWGOA_PvsAOSzGmY2nLjpxeA-R5uKHfmDxsKA0aQzOr85cKunKFEdvxPs5Ay3BvBA8yszf39u1dxat1lOEzbfFZj0NoPZs0YpnL1J0pqWiaIQmffJQwjUvP-aUiBujWzOohVORHJ7RCsiZOaIewk7pBKM7c9n5Aq4urbcu9uzjgxuSJ3Oqf4kfHOwHZAXWVFhz43jBBlEpLCzNelz16rnZ6SRydUxip9Rc-2erlzU6JF5_SGMWQrGRdX6zmJjxawNJjg-Fwosw1yK5Y2j2wRmpHhFRTfkkydFX2wcdFk8ziysHf5YdSZQGM50VHAK5b5TSgmRzKdaFaMc.gJXZTEjTlJCniRUAryhJ_bFhveljmR07qZ5qayt5j4k&dib_tag=se&keywords=beauty+of+joseon&qid=1742561232&sprefix=beau%2Caps%2C96&sr=8-5",
    "https://www.amazon.co.uk/COSRX-Moisturizing-Secretion-Moisturiser-Hydration/dp/B01LEJ5MSK/ref=sr_1_5_pp?crid=3BK232CP9A6NI&dib=eyJ2IjoiMSJ9.7y0DkqpxhuayDTErhQ-pWPZroxpIMiQ4EoQhUbVafdcnDDmQ2M5HrZqjSsszZ2bF_u92vBSvc38qU8gXeRP0cYmrTs8-B7W_h8dQnifpsy-97lbPYEQgN7uhP8W5pfV5ru7SUKTGhaNWB3j4q8se_7b8qHQmtjvrimpzoUwAZKDbzKvETQwp_xIDqnI-Rjpqcz_-IeXzO6aodWzFwDPMgVn5j8TftjBdXsPWs2b2odTlBbIw8FbMKxoFWZxMUKIKUtMBqHUuRGO3joPwmQl7Zv-prAimSo86bTW7AZAJ2fsX2hTpisT18tN-9iXGUOypsL7l02njDJQU7fTIn38H_tS1nqba0IrcrccYJ9Qn1YrhVXB0Qx49sOGwUR_zZTRgwD538BXVg0gqLee3XwNxH-NsxIK1VsTuVeNzJLCiO3c5Q1Wm5NJvyRR5lhth1OWB.fpwXrfzkR7HpX5p6UPLGt2He98bLHXXiKQDJSFpvxa4&dib_tag=se&keywords=snail+mucin&qid=1742561264&sprefix=snail%2Caps%2C105&sr=8-5#customerReviews",
    "https://www.amazon.co.uk/PURITO-Centella-Unscented-Soothing-Cruelty-Free/dp/B0CST174J1/ref=sr_1_5_pp?crid=1ATJO1QZ1S49S&dib=eyJ2IjoiMSJ9.z4IwHzaoj0X6gk7mLYqpUAXf75uKr0ObgmcTM7nfwoKdt9plbShKeMFgCqnyeHCRAPWN1qAGs2LfdqQi5smf09tl6FD1kl_IXmeUuDLd45YBI9ohnQb6T0qpqCTT5qqweebwX8k0KgDYMgTGuQOqWh2utfBlO-j40AoV2u3tXTky1yD_bmR9z8KYRsgC85Tjcl_WtT5rytLVpobfWQtO60ox_QmOY8jUSRlTNjPRWaIICz4vUrLqSxTxtadGFMPsMl7N2qNvch6r9eMzk5ShXbvp7RaxHiziJsXcEDUqFzTWbHuDLSRxZkReKXd-0vYvWzdOkEHv6X2YC9vBhokbydmFEYF5naQ7UWZ1UdQhxYNwK2Lhz5bjBLdSiH5imP7c59dPwldugA1ZCH3adn_MbTCqCYjBI2JVhGjmwJ4WSVvyvDXmzNmJG6khgjwPbqIH.4ZMSZJA8ERa3sLs9WIRcuYGRkBH8rR3wmKiKEc_2PMM&dib_tag=se&keywords=purito%2Bcentella%2Bunscented%2Bserum&qid=1742561341&sprefix=purito%2B%2Caps%2C101&sr=8-5&th=1",
    "https://www.amazon.co.uk/dp/B08PVDZQMD?ref=nb_sb_ss_w_as-reorder_k0_1_11&amp=&crid=2046HRR1JXZXM&sprefix=moisturiser&th=1"
]

def get_amazon_price(dom):

    try:
        
        price = dom.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')[0]
        price = price.replace(',', '').replace('£', '').replace('.00', '')
        return int(price)
    except Exception as e:
        price = 'Not Available'
        return None

def get_product_name(dom):
    try:
        name = dom.xpath('//span[@id="productTitle"]/text()')
        [name.strip() for name in name]
        return name[0]
    except Exception as e:
        name = 'Not Available'
        return None

def get_master_price(url):
    for row in df.itertuples():
        if row.url == url:
            return row.price
    return None

#lists for storing products with a price drop (name and url)
price_drop_products = [] 
price_drop_list_url =[]

#going through each page, get current price and compare it against the file in data extracter file
#and see if there is a change in price of more than 10%. if true, it gets added to the lists
for product_url in amazon_urls:

    response = requests.get(product_url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    main_dom = et.HTML(str(soup))

    price = get_amazon_price(main_dom)
    product_name = get_product_name(main_dom)
    df = pd.read_csv('master_Data.csv', encoding='cp1252')

    master_price = get_master_price(product_url)
    if master_price is not None and price is not None and price < master_price:
        change_percentage = round((get_master_price(product_url) - price) * 100 / get_master_price(product_url))

        if change_percentage > 10:
            print(' There is a {}'.format(change_percentage), '% drop in price for {}'.format(product_name))
            print('Click here to purchase {}'.format(product_url))
            price_drop_products.append(product_name)
            price_drop_list_url.append(product_url)

print(f"Checking product: {product_name}, Current Price: {price}, Master Price: {master_price}")

print(f"Scraped price for {product_name}: {price}")


#if no price chnge, exit the program
if len(price_drop_products) == 0:
    sys.exit('No Price drop found')

#if there is a change, using Twilio API and send a message.
messege = "There is a drop in price for " \
"{}".format(len(price_drop_products)) + " products." + "Click to purchase"

for items in price_drop_list_url:
    messege = messege + "\n" + items

account_sid = 'Add your account sid'
auth_token = 'Add your auth token'

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='07947644437',
    body=messege,
    to='07947644437'
)
sys.exit('Price drop found')
