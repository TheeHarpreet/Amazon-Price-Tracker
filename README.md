# 🛍️ Amazon Price Tracker 📉
This project helps you track product prices on Amazon and notifies you via SMS if there is a significant price drop! 💸

## 🚀 Features
- Track multiple Amazon products: Enter product URLs to track prices.

- SMS Notification: Receive SMS alerts via Twilio when there's a price drop of more than 10%. 📱

- Price Comparison: Compare the current price with a previously recorded price from a CSV file. 📊

- Automatic Price Update: Automatically fetch and check prices at regular intervals.

## 🛠️ Requirements
Before running the code, make sure you have the following installed:

- Python 3.x

- requests

- beautifulsoup4

- lxml

- twilio

- pandas

Install the dependencies using pip:

```bash
pip install requests beautifulsoup4 lxml twilio pandas
```
## 🔑 Twilio Setup
1. Sign up at Twilio to get your account SID, Auth Token, and a Twilio phone number.

2. Replace the following placeholders in the code:

- 'Add your account sid'

- 'Add your auth token'

- 'Add your twilio phone number'

- 'Add your personal phone number'

## 📜 File Structure
Here are the key files in the project:

### amazon_price_tracker.py 📝
This file handles:

- Scraping product prices from Amazon.

- Comparing the current price to the saved price.

- Sending an SMS via Twilio when a price drop is detected.

### data_extractor.py 📥
This script:

- Scrapes product details (name, price, URL) from Amazon.

- Stores the data in a CSV file for future price comparison.

### auto_price_check.py ⏲️
- This is the script for automatically checking prices every 1 hour:

- It runs in the background, fetching prices and comparing them to the stored prices every hour.

- If there is a price drop of more than 10%, you will receive an SMS alert.

## 💻 How to Run
1. Extract Product Data: Run the data_extractor.py script to gather product names, prices, and URLs from Amazon and save them to a CSV file:

```bash
python data_extractor.py
```
2. Track Prices: Run the amazon_price_tracker.py script to check if any of the tracked products have experienced a price drop of more than 10%. You will receive an SMS if there is a drop.

```bash
python amazon_price_tracker.py
```

3. Automatically Track Prices Every Hour: Run the price_checker.py script to automatically check the prices every hour:

```bash
python price_checker.py
```
This script will keep checking the prices of your products every hour and notify you via SMS if any price drops by more than 10%.

## Example Output 💬
When a price drop is detected, you will see the following:

```bash
There is a 12% drop in price for HyperX Cloud III Wireless Headset
Click here to purchase: https://www.amazon.com/HyperX-Cloud-III-Wireless-headset/dp/B0CBQXGZ85
```
And you will receive an SMS like this:

```bash
There is a drop in price for 1 products. Click to purchase
- https://www.amazon.com/HyperX-Cloud-III-Wireless-headset/dp/B0CBQXGZ85
```

## 💡 Tips
- You can add as many product URLs to the amazon_urls list as you want to track.

- Make sure to keep your CSV file updated with accurate pricing to get the best price drop alerts.

##🚨 Disclaimer
- Be mindful of any restrictions that Amazon may impose on frequent scraping.

- Ensure that you use your Twilio credentials securely and don’t share them publicly. 🔒

## 📞 Contact
If you have any questions or run into issues, feel free to contact me! 📧
