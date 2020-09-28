from bs4 import BeautifulSoup
import requests
import json

# Extracting html code from the web
url = "https://kurs.web.id/api"
page = requests.get(url)
output = BeautifulSoup(page.content, 'html.parser')

# Extracting the name of all banks and its code in one list
content = []
for bank in output.find_all('td'):
    content.append(bank.text)
content = content[-40:]

# Listing bank name and its code in separated list
bank = []
code = []
for i in range(0,len(content)-1,2):
    bank.append(content[i])
    code.append(content[i+1])
