from bs4 import BeautifulSoup as bs
import requests

link = 'https://letterboxd.com/gojizillakong/list/favourite-movies/'

req = requests.get(link)

soup = bs(req.text, 'html.parser')
print(soup)
f = open("html_soup.txt", 'w')
f.write(soup.prettify())
f.close()