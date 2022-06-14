import requests
from bs4 import BeautifulSoup

text= "porn"
url = 'https://google.com/search?q=' + text
  
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
  
# find all objects with class "iUh30 tjvcx"
# and store them in a variable, soup.
soup=BeautifulSoup( request_result.text, 'html.parser' )
print(soup)