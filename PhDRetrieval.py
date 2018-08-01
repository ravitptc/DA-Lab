import requests
from bs4 import BeautifulSoup
url = 'http://psgim.ac.in/2017/01/full-time-faculty/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "lxml")
table = soup.find()
for row in table.findAll('h4'):
    cur = row.text
    if(cur[:2] == "Dr" or cur[:2] == "DR"):
        print(cur)
