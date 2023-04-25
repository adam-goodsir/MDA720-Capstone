#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import requests


# In[2]:


# Developer API key
MY_API_KEY= "cp9bHlVDhqzBZkAHflaC-QkCncAu3-cYQOTg8nNxMbAOUBcJoRJBEkCon6Ip8dhq1F-wpN9z8WuaZWeV5YqTvL8OpzvuNwJlM7I8p-OdDp_t3NdTsX7NgehrVncwZHYx"
# What you are searching for
DEFAULT_TERM = 'Car Dealerships'
# Business location
DEFAULT_LOCATION = 'Okemos, MI'
# Maximum number of results to return
SEARCH_LIMIT = 10
 
# Busines search end point
url = 'https://api.yelp.com/v3/businesses/search'
# Header should contain the API key
headers = {'Authorization': 'Bearer {}'.format(MY_API_KEY)}
# Search parameters
url_params = {
	'term': DEFAULT_TERM, 
	'location': DEFAULT_LOCATION, 
	'limit': SEARCH_LIMIT
	}
 
# Call the API
response = requests.request('GET', url, headers=headers, params=url_params)

restaurants = []
for business in response.json()["businesses"]:
    print("{:30}  {:5}  {:20}  {:10}".format(
        business["name"], 
        business["rating"], 
        business["location"]["display_address"][0], 
        business["display_phone"]))
    restaurants.append(restaurants)


# In[5]:


# Developer API key
MY_API_KEY= "cp9bHlVDhqzBZkAHflaC-QkCncAu3-cYQOTg8nNxMbAOUBcJoRJBEkCon6Ip8dhq1F-wpN9z8WuaZWeV5YqTvL8OpzvuNwJlM7I8p-OdDp_t3NdTsX7NgehrVncwZHYx"
# What you are searching for
DEFAULT_TERM = 'Car Dealerships'
# Business location
DEFAULT_LOCATION = 'Birmingham, MI'
# Maximum number of results to return
SEARCH_LIMIT = 10
 
# Busines search end point
url = 'https://api.yelp.com/v3/businesses/search'
# Header should contain the API key
headers = {'Authorization': 'Bearer {}'.format(MY_API_KEY)}
# Search parameters
url_params = {
	'term': DEFAULT_TERM, 
	'location': DEFAULT_LOCATION, 
	'limit': SEARCH_LIMIT
	}
 
# Call the API
response = requests.request('GET', url, headers=headers, params=url_params)

restaurants = []
for business in response.json()["businesses"]:
    print("{:30}  {:5}  {:20}  {:10}".format(
        business["name"], 
        business["rating"], 
        business["location"]["display_address"][0], 
        business["display_phone"]))
    restaurants.append(restaurants)


# In[3]:


df = pd.DataFrame(response.json()["businesses"])


# In[4]:


df = df[["name", "rating", "location", "display_phone"]]


# In[5]:


df.to_excel("dealerships_Okemos.xlsx", index=False) 


# In[9]:


df1= pd.DataFrame(response.json()["businesses"])


# In[10]:


df1 = df1[["name", "rating", "location", "display_phone"]]


# In[11]:


df1.to_excel("dealerships_Birmingham.xlsx", index=False)

