from bs4 import BeautifulSoup
import pandas as pd
import requests
import json


##### SCRAPPING BANK CODE #####
# Extracting html code from the web
url = "https://kurs.web.id/api"
page = requests.get(url)
output = BeautifulSoup(page.content, 'html.parser')
# Extracting the name of all banks and its code in one list
content = []
for bank in output.find_all('td'):
    content.append(bank.text)
content = content[-40:]
# Display bank name and code
code = []
print('\nHere is the list of bank name and bank code.')
for i in range(0,len(content)-1,2):
    print(content[i] + ': ' + content[i+1])
    code.append(content[i+1])


# Command the user to input their bank code
yourbank = input("\nMy bank code is: ")
a = yourbank.lower() in code

# Store the token first
token = '3JGx7rYwr5xjrfhcBmbiA0aeLiLhUwVyzvhzDbfu'


while True:

    if a == True :
        ##### SCRAPPING CURRENCY #####
        # Scrapping available currency on the selected bank
        urlbank = f'https://kurs.web.id/bank/{yourbank.lower()}'
        page = requests.get(urlbank)
        out = BeautifulSoup(page.content, 'html.parser')
        print(f"\nAvailable currency in {yourbank.upper()} are:")
        avail = []
        for curr in out.find_all('option', class_ = 'price'):
            avail.append(curr.text)
        for i in range(int(len(avail)/2)):
            print(avail[i])

        # Taking Action
        print("\nWhat do you want to do?\n1. Convert IDR to Foreign Currency\n2. Convert Foreign Currency to IDR\n3. Quit")
        opt = int(input("Choose one action [1/2/3]: "))

        while True:

            if opt == 1:
                # Command the user to input their currency and total money
                print("\n-----Conversion from IDR to Foreign Currency-----")
                currency = input("I want to convert from IDR to: ")
                money = float(input("Total money I want to change is: "))

                while True:

                    if ((currency.upper() in avail) == False) and (money <= 0):
                        print('\nPlease enter correct value of currency and total money.')
                        currency = input("I want to convert from IDR to: ")
                        money = float(input("Total money I want to change is: "))
                    elif ((currency.upper() in avail) == False):
                        print('\nPlease enter correct value of currency.')
                        currency = input("I want to convert from IDR to: ")
                    elif (money <= 0):
                        print('\nPlease enter correct value of currency and total money.')
                        money = float(input("Total money I want to change is: "))
                    else:
                        # Extract data from kurs.web.id
                        url = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank.lower()}&matauang={currency.lower()}"
                        data = requests.get(url)
                        output = data.json()

                        # Display conversion1
                        kurs_jual = output['jual']
                        print(f'Your fund IDR {money} is worth {currency.upper()} {money/kurs_jual}')

                        # Go back to option
                        print("\nWhat else do you want to do?\n1. Convert IDR to Foreign Currency\n2. Convert Foreign Currency to IDR\n3. Quit")
                        opt = int(input("Choose one action [1/2/3]: "))
                        break

            elif opt == 2:
                # Command the user to input their currency and total money
                print("-----Conversion from Foreign Currency to IDR -----")
                currency_ = input("My money is in: ")
                money_ = float(input("Total money I want to change is: "))

                # Extract data from kurs.web.id
                url_ = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank.lower()}&matauang={currency_.lower()}"
                data_ = requests.get(url_)
                output_ = data_.json()

                # Display conversion2
                kurs_beli = output_['beli']
                print(f'Your fund {currency_.upper()} {money_} is worth IDR {money_*kurs_beli}')

                # Go back to option
                print("\nWhat else do you want to do?\n1. Convert IDR to Foreign Currency\n2. Convert Foreign Currency to IDR\n3. Quit")
                opt = int(input("Choose one action [1/2/3]: "))

            elif opt == 3:
                print("Thank you for using our service. See you on the next transaction.")
                break

            else:
                print("Sorry, we did not understand that.")
                print("\nWhat do you want to do?\n1. Convert IDR to Foreign Currency\n2. Convert Foreign Currency to IDR\n3. Quit")
                opt = int(input("Choose one action [1/2/3]: "))

        break
    else:
        print('Sorry, we did not recognize that bank. Please re-enter your bank code.')
        bank = input("My bank code is: ")
        a = bank.lower() in code