#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[9]:


response = requests.get('https://63.ru/')
response


# In[10]:


print(response.text)


# In[11]:


print(response.status_code)


# In[16]:


respone = requests.get('https://xseo.in/asn')
print(respone.text)


# In[40]:


response = requests.get('https://catfact.ninja/facts')


json = response.json()
print(json)


# In[44]:


print(json.keys()) 


# In[47]:


print(json['from'], json['total'])


# In[56]:


for x in range(3):
    response = requests.get('https://catfact.ninja/facts')
    json = response.json()
    print(x , json['data'])


# In[ ]:




