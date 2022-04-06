# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import re


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

questionList = []

a_file = open("medList.txt", "r")

fileobj=open("medList.txt")
it=iter(fileobj)
lines=[]
while True:
    try:
        line=next(it)
        line=line.strip()
        lines.append(line)
    except StopIteration:
        break

def getPrices(tag):
    url = f'https://www.goodrx.com/{tag}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)

    questions = soup.find_all('div', {'class': 'pageContainer-2NS57 desktop-3xeHJ'})
    
    for item in questions:

        try:
            question = {
            'link' : item.find('h1', {'class': 'titleStyles-i9mVW'}).text,
            'Retail_price' : item.find('span', {'class': 'retailPriceStrikeSavings-2k8q6'}).text,
            'Discount_price' : item.find('div', {'class': 'display-2N4dk'}).text,
            }
        except Exception as e:
            print(e)
            break
        questionList.append(question)
        break
    return


for x in range(2):
    getPrices(lines[x])
    time.sleep(10)



