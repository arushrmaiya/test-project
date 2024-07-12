from bs4 import BeautifulSoup as bs
import requests

link = 'https://letterboxd.com/gojizillakong/'

req = requests.get(link)

soup = bs(req.text, 'html.parser')
print(soup)