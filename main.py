import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Abraham_Lincoln'
r = requests.get(url)
conteudoHtml = r.text
htmlSoup = BeautifulSoup(conteudoHtml, features="lxml")
print(htmlSoup.find('h1'))

