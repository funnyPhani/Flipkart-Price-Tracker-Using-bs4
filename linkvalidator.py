import requests as r
from bs4 import BeautifulSoup as bs


# In[2]:


def check(url):
    page = r.get(url)
    soup = bs(page.content,"html.parser")
    if soup.find_all("div",{"class":"_1vC4OE _3qQ9m1"}):
        return True
    else:
        return False


# In[ ]:



