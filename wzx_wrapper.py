import requests, json
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = "https://api.wazirx.com/api/v2/tickers"

content = requests.get(url, headers=headers)
data = content.json()
print(data)
