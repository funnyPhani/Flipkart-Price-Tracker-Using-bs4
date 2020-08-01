#!/usr/bin/env python
# coding: utf-8

# This is all on press of the button url will be inputted by user through text field, pricing and email id will be then stored to the database

# In[ ]:


import Scrapper as sc
from pymongo import MongoClient


# In[ ]:


#Establish connection with mongodb
mongoclient = MongoClient('mongodb+srv://main-user:ILoveBurgers@customercluster.st0fr.mongodb.net/customer?retryWrites=true&w=majority')
db = mongoclient.get_database('customer')
records = db.data


# In[ ]:


#Save data to db
def insertdata(i,email,link,reduce_price):
    data = {'_id':i,'email':email,'link':link,'reduce_price':reduce_price}
    records.insert_one(data)

