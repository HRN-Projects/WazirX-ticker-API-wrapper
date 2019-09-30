import requests, json, time
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = "https://api.wazirx.com/api/v2/tickers"

coin = (input("Coin : ") + "inr").lower()

def find_coin_data(coin, data):
	return data[coin]

while True:
	content = requests.get(url, headers=headers)
	data = content.json()

	final = find_coin_data(coin, data)
	print(final)

	time.sleep(1)
