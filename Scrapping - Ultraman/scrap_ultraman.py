from bs4 import BeautifulSoup
import requests
import json

## METHOD TO EXTRACT THE PAGE ONLINE ##
url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'    #insert the url of the subject
page = requests.get(url)     #get into the website
out = BeautifulSoup(page.content, 'html.parser')    #inspect the page
# print(out.prettify)     #list html code in order (pretty way)

## SCRAPING CHARACTER NAMES ##
character = []    #creating empty list to be filled with characters
for name in out.find_all('strong'):     #find item in 'strong' brackets
    character.append(name.text)     #insert items into 'character' list

## CLASSIFY HEROS AND VILLAINS NAME ##
hero = character[2:36]     #extracting hero names from character list using index
villain = character[37:110]     #extracting villain names from character list using index

## CREATING DICTIONARY OF HERO NO AND NAME ##
keyhero = []
valuehero = []
for i in hero:
    keyhero.append(i[:2])
    valuehero.append(i[3:])
ultraman = dict(zip(keyhero, valuehero))

## CREATING DICTIONARY OF VILLAIN NO AND NAME ##
keyvillain = []
valuevillain = []
for j in villain:
    keyvillain.append(j[:2])
    valuevillain.append(j[3:])
monster = dict(zip(keyvillain, valuevillain))

## MAKING JSON FILE ##
scrap = [dict(zip(['Ultraman','Monsters'],[ultraman, monster]))]
with open('scrap.json', 'w') as file:
    json.dump(scrap, file)

print(scrap)