import requests

# Display the description of the program
print("Welcome to Tomatos App. What can we help?")
print("1. Find nearest restaurant.\n2. Display daily menu on a restaurant\n3. Quit")
opt1 = input("Please enter the number of your action [1/2/3]: ")

# Storing API key
key = '792915195d49f3c035fd1cb56aacd2b4'

# Actions
while True:
    if opt1 == '1':
        city = input("Please input your city name: ")
        count = int(input("How many results do you want to show? "))
        urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
        ext1 = requests.get(urlcity, headers = {'user-key': key})
        data1 = ext1.json()
        # Checking
        while True:
            if len(data1['location_suggestions']) == 1 and (count > 0):
                cityid = data1['location_suggestions'][0]['id']
                urlresto = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&count={count}'
                ext2 = requests.get(urlresto, headers = {'user-key': key})
                data2 = ext2.json()
                for i in range(len(data2['restaurants'])):
                    print(f'\n-----  {data2["restaurants"][i]["restaurant"]["name"]}  -----')
                    print(f'Establishment: {data2["restaurants"][i]["restaurant"]["establishment"][0]}')
                    print(f'Cuisine type: {data2["restaurants"][i]["restaurant"]["cuisines"]}')
                    print(f'Address: {data2["restaurants"][i]["restaurant"]["location"]["address"]}')
                    print(f'Telp. No. : {data2["restaurants"][i]["restaurant"]["phone_numbers"]}')
                    print(f'Rating: {data2["restaurants"][i]["restaurant"]["user_rating"]["aggregate_rating"]}')
                    print(f'Reviews: {data2["restaurants"][i]["restaurant"]["all_reviews_count"]}')
                print("\nWhat else you want to do?")
                print("1. Find nearest restaurant.\n2. Display daily menu on a restaurant\n3. Quit")
                opt1 = input("Please enter the number of your action [1/2/3]: ")
                break
            elif len(data1['location_suggestions']) == 1 and (count <= 0):
                print("\nYour input on # of displayed result is invalid.")
                count = int(input("How many results do you want to show? "))
            elif len(data1['location_suggestions']) != 1 and (count > 0):
                print("\nYou entered an unknown city.")
                city = input("Please try another city: ")
                urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
                ext1 = requests.get(urlcity, headers = {'user-key': key})
                data1 = ext1.json()
            else:
                print("\nYou messed up. Try again.")
                city = input("Please input your city name: ")
                count = int(input("How many results do you want to show? "))
                urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
                ext1 = requests.get(urlcity, headers = {'user-key': key})
                data1 = ext1.json()

    elif opt1 == '2':
        resto = input("Please enter the restaurant name: ")
        city = input("Please enter your city: ")
        count = int(input("How many results do you want to show? "))
        urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
        ext1 = requests.get(urlcity, headers = {'user-key': key})
        data1 = ext1.json()
        while True:
            if len(data1['location_suggestions']) == 1 and (count > 0):
                cityid = data1['location_suggestions'][0]['id']
                urlresto = f'https://developers.zomato.com/api/v2.1/search?entity_id={cityid}&entity_type=city&q={resto}&count=1'
                ext2 = requests.get(urlresto, headers = {'user-key': key})
                data2 = ext2.json()
                restoid = data2['restaurants'][0]['restaurant']['id']
                urlmenu = f'https://developers.zomato.com/api/v2.1/dailymenu?res_id={restoid}'
                ext3 = requests.get(urlmenu, headers = {'user-key': key})
                data3 = ext3.json()
                if data3['status'] == "success":
                    if count <= len(data3['daily_menus'][0]['daily_menu']['dishes']):
                        for i in range(count):
                            print(f"Menu {i+1}")
                            print(f"Dish name: {data3['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['name']}")
                            print(f"Price: {data3['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['price']}")
                    else:
                        for i in range(len(data3['daily_menus'][0]['daily_menu']['dishes'])):
                            print(f"Menu {i+1}")
                            print(f"Dish name: {data3['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['name']}")
                            print(f"Price: {data3['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['price']}")
                    print("\nWhat else you want to do?")
                    print("1. Find nearest restaurant.\n2. Display daily menu on a restaurant\n3. Quit")
                    opt1 = input("Please enter the number of your action [1/2/3]: ")
                    break
                else:
                    print("There is no daily menu in this restaurant")
                    print("\nWhat else you want to do?")
                    print("1. Find nearest restaurant.\n2. Display daily menu on a restaurant\n3. Quit")
                    opt1 = input("Please enter the number of your action [1/2/3]: ")
                    break
            elif len(data1['location_suggestions']) == 1 and (count <= 0):
                print("\nYour input on # of displayed result is invalid.")
                count = int(input("How many results do you want to show? "))
            elif len(data1['location_suggestions']) != 1 and (count > 0):
                print("\nYou entered an unknown city.")
                city = input("Please try another city: ")
                urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
                ext1 = requests.get(urlcity, headers = {'user-key': key})
                data1 = ext1.json()
            else:
                print("\nYou messed up. Try again.")
                city = input("Please input your city name: ")
                count = int(input("How many results do you want to show? "))
                urlcity = f'https://developers.zomato.com/api/v2.1/cities?q={city}&count=1'
                ext1 = requests.get(urlcity, headers = {'user-key': key})
                data1 = ext1.json()

    elif opt1 == '3':
        print("Thank you for using our service.")
        break

    else:
        print("Sorry, we did not understand that.")
        print("1. Find nearest restaurant.\n2. Display daily menu on a restaurant\n3. Quit")
        opt1 = input("What do you want to do? [1/2/3] ")