#! python3

import os
import requests
import bs4 as bs
import urllib.request
import re


url = 'https://www.foodnetwork.com/recipes/food-network-kitchen/cheesecake-recipe2-2011459'
device = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

#os.makedirs('name', exist_ok=True)

headers = {'User-Agent': device}
resp = requests.get(url, headers=headers)
soup = bs.BeautifulSoup(resp.text, 'lxml')
images = soup.findAll('img',{"src":True})

i=1
for image in images:
    if ".com" not in image['src']:
        continue
    if image['src'].startswith('//'):
        imageSource = image['src'][2:]
        imageSource = "http://" + imageSource
    else:
        imageSource = image['src']
    print(imageSource)
        
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', device)]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imageSource, str(i) + ".jpg")
    i +=1
