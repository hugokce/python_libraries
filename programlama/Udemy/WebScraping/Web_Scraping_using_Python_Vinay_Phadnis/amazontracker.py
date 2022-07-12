import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Blue-Yeti-USB-Microphone-Silver/dp/B002VA464S'
r = requests.get(url)
print(r)

html = BeautifulSoup(r.content,'html.parser')

print(html)

