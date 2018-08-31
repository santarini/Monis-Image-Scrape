#! python3

import os
import csv
import requests
import bs4 as bs
import urllib.request
import re

i=1

with open("input.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = (row['URL'])
        device = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        #os.makedirs('name', exist_ok=True)
        headers = {'User-Agent': device}
        resp = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        images = soup.findAll('img',{"src":True})

        
        for image in images:
            ext = [".com", ".org" ".net"]
            if not(any(x in image['src'] for x in ext)):
                print("Skipped " + imageSource)
                continue
            if image['src'].startswith('//'):
                imageSource = image['src'][2:]
                imageSource = "http://" + imageSource
            else:
                imageSource = image['src']
            #print(imageSource)
                
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', device)]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imageSource, str(i) + ".jpg")
            i +=1
