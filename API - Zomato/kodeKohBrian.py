import requests

key = "0aa5d9130201117c126a4e43a03b0e01"
print("SELAMAT DATANG DI APLIKASI ZOMATOS", "SILAHKAN PILIH OPSI:",f"{' '*2} 1. Cari Restoran", f"{' '*2} 2. Menu Harian", sep = '\n')
option = input("Please pick an option:")

while option.isdigit() == False or (int(option) < 1 or int(option) > 2):
  print("Sorry, wrong input")
  option = input("Please pick an option:")

# ======================================== CARI RESTORAN
if option == '1':
  input_city = input("Masukkan nama kota: ")
  try:
    # selama inputannya digit, looping terus
    while input_city.isdigit() == True or (int(input_city) <= 0 or int(input_city) > 1):
      print("Mohon masukkan teks, bukan angka.")
      input_city = input("Masukkan nama kota: ")
  # kalo inputannya udah pasti string
  except ValueError:
    header_info = {"user-key" : key}
    url_city = f"https://developers.zomato.com/api/v2.1/cities?q={input_city}" #GET/cities
    data = requests.get(url_city, headers = header_info)
    zomato_cities = data.json()
    # print(zomato)

  # ambil 'city id' buat next process
  try:
    city_id = zomato_cities['location_suggestions'][0]['id']
  except IndexError:
    print("Kota tidak ada")
    input_city = input("Masukkan nama kota: ") # coba tweak lagi
  
  resto_show = input("Masukkan jumlah nama restoran yang ingin ditampilkan: ")
  while resto_show.isdigit() == False:
    print("Mohon masukkan angka, bukan teks")
    resto_show = input("Masukkan jumlah nama restoran yang ingin ditampilkan: ")
  
  print("", f"--- SEARCH RESULTS FOR {input_city.upper()}: ---", sep = '\n')
  url_resto = f"https://developers.zomato.com/api/v2.1/search?entity_id={city_id}&entity_type=city&start=0&count={resto_show}" #GET/search
  data_resto = requests.get(url_resto, headers = header_info)
  zomato_resto = data_resto.json()
  for i in range(int(resto_show)):
    resto = zomato_resto['restaurants'][i]['restaurant']
    print(f"{i+1}.")
    print(f"Restaurant Name: {resto['name']}")
    print(f"Establishment Type: {resto['establishment'][0]}")
    print(f"Cuisine Type: {resto['cuisines'][:]}")
    print(f"Address: {resto['location']['address']}")
    print(f"Phone Number: {resto['phone_numbers']}")
    print(f"Average Rating: {resto['user_rating']['aggregate_rating']}")
    print(f"Total Review: {resto['all_reviews_count']}")

    url_dmenu = f"https://developers.zomato.com/api/v2.1/dailymenu?res_id={resto['id']}" #GET/dailymenu
    data_dmenu = requests.get(url_dmenu, headers = header_info)
    dmenu = data_dmenu.json()
    try:
      print(f"Daily Menu: {dmenu['daily_menus']}")
    except KeyError:
      print("Maaf, tidak tersedia Daily Menu pada restoran ini.")
    print('\n')

# ============================ MENU HARIAN
if option == '2':
  restaurant_name = input("Masukkan nama restoran: ")
  while restaurant_name.isdigit() == True:
    print("Mohon masukkan teks saja")
    restaurant_name = input("Masukkan nama restoran: ")
  
  city_name = input("Masukkan nama kota: ")
  while city_name.isdigit() == True:
    print("Mohon masukkan teks saja")
    city_name = input("Masukkan nama kota: ")

  menu_show = input("Masukkan jumlah menu yang ingin ditampilkan: ")
  while menu_show.isdigit() == False:
    print("Mohon masukkan angka saja")
    menu_show = input("Masukkan jumlah menu yang ingin ditampilkan: ")

  url_city = f"https://developers.zomato.com/api/v2.1/cities?q={city_name}" #GET/cities
  header_info = {"user-key" : key}
  data = requests.get(url_city, headers = header_info)
  city = data.json()
  # print(city)
  try:
    city_id = city['location_suggestions'][0]['id']
  except IndexError:
    print("Kota tidak tersedia")
  
  url_menu = f"https://developers.zomato.com/api/v2.1/search?entity_id={city_id}&entity_type=city&q={restaurant_name}&start=0&count={menu_show}" #GET/search
  data_menu = requests.get(url_menu, headers = header_info)
  menu = data_menu.json()

  res_id = menu['restaurants'][0]['restaurant']['id']
  url_dmenu = f"https://developers.zomato.com/api/v2.1/dailymenu?res_id={res_id}" #GET/dailymenu
  data_dmenu = requests.get(url_dmenu, headers = header_info)
  dmenu = data_dmenu.json()
  # print(dmenu)

  print('\n')
  print(f"--- MENU {restaurant_name.upper()} di {city_name.capitalize()} HARI INI: ---")
  try:
    daily_menu = dmenu['daily_menus'][0]['daily_menu']['dishes']
    for i in range(int(menu_show)):
      print(f"{' '*2}{i+1}. {daily_menu[i]['dish']['name']}")
  except KeyError:
    print("Menu tidak tersedia")
  
  try:
    print(f"Jumlah menu di {restaurant_name.upper()} {city_name.capitalize()} adalah {len(daily_menu)} menu.")
  except:
    print("Tidak bisa menjumlah menu karena menu tidak tersedia")