from bs4 import BeautifulSoup
import requests
import mysql.connector


############ SCRAPPING THE WEBSITE ###########

# Extracting Page
url = 'http://digidb.io/digimon-list/'
page = requests.get(url)
ext = BeautifulSoup(page.content, 'html.parser')

# Extracting Data (without image link)
data = []
for i in ext.find_all('tbody'):
    for j in i.find_all('tr'):
        for k in j.find_all('td'):
            data.append(k.text)
Digi_ID = list(range(1,int((len(data)/13))+1))

# Extracting Image Link
link = []
for i in ext.find_all('img'):
    link.append(i['src'])
img = []
for i in range(2, 343):
    img.append(link[i])

# Creating Dataset
mydata = []
count = list(range(0,len(data),13))
for j in range(len(Digi_ID)):
    i = count[j]
    mytuple = f"({Digi_ID[j]}, '{img[j]}', '{data[i+1]}', '{data[i+2]}', '{data[i+3]}', '{data[i+4]}', {data[i+5]}, {data[i+6]}, {data[i+7]}, {data[i+8]}, {data[i+9]}, {data[i+10]}, {data[i+11]}, {data[i+12]})"
    mydata.append(mytuple)



############ CREATING SQL TABLE ###########

# Connecting to MySQL
user = {
    'user': 'root',
    'password': 'Ch3C##h4$',
    'host': 'localhost'}
myDB = mysql.connector.connect(**user)
cur = myDB.cursor()

# Creating Database
cur.execute("DROP DATABASE digimon")
cur.execute("CREATE DATABASE digimon")
cur.execute("USE digimon")

# Creating table
query1 = """CREATE TABLE profiles (Digimon_ID SMALLINT, Image_Link CHAR(50),
Digimon_Name CHAR(30), Digimon_Stage CHAR(20), Digimon_Type CHAR(20), Attribute CHAR(20), Memory SMALLINT, Equip_Slots SMALLINT, HP SMALLINT, SP SMALLINT, Attack SMALLINT, Defense SMALLINT, Intelligence SMALLINT, Speed SMALLINT)"""
cur.execute(query1)
myDB.commit()

# Data Entry
for i in mydata:
    query2 = f"INSERT INTO profiles VALUES {i}"
    cur.execute(query2)
    myDB.commit()