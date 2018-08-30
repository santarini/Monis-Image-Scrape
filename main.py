#!Python
import requests
import bs4 as bs
import urllib.request
import re

url = 'https://www.bbcgoodfood.com/recipes/2239/ultimate-fish-cakes'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
resp = requests.get(url, headers=headers)
soup = bs.BeautifulSoup(resp.text, 'lxml')
images = soup.findAll('img')

i=1
for image in images:
    print(image['src'])
    urllib.request.urlretrieve(image['src'], str(i) + ".jpg")
    i +=1
