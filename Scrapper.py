#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as r
from bs4 import BeautifulSoup as bs


# In[2]:


def getprice(url):
    #scrap the price from urlf
    page = r.get(url)
    soup = bs(page.content,"html.parser")
    price = soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text
    price = list(price)
    if "," in price:
        price.remove(",")
    else:
        pass
    price.remove("₹")
    price = ''.join([str(elem) for elem in price]) 
    return int(price)

