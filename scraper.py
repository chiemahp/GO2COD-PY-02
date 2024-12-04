import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://go2cod.com.et/')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

