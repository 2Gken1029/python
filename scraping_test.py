#!/usr/bin/env python3
# coding: utf-8

import requests
from lxml import html
from bs4 import  BeautifulSoup

url = 'http://www.web-aquarium.net/'

res = requests.get(url)
res.encoding = res.apparent_encoding
raw_html = res.text
soup = BeautifulSoup(raw_html, "html.parser")

import re
raw_aquarium_list = soup.find_all("a", href=re.compile("aquarium/aq_"))
aquarium_list_url = ['http://www.web-aquarium.net/' + data.attrs['href'] for data in raw_aquarium_list]


import time
aquarium_list = []

for url in aquarium_list_url:
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    raw_html = res.text
    soup = BeautifulSoup(raw_html, "html.parser")
    data = soup.find_all(id="data")
    name = soup.find(id="aqua_name").text
    if data == []:
        continue
    aquarium_list.append([name, data[1].text.replace('\n', '').replace('\t', ''), data[2].text])
    time.sleep(1)

print(aquarium_list)