import requests

# Printing the description of the program
print("This program displays weather data of a city")

# Providing API Key
key = 'a7c8ced238b4a723e31ddb78fbf50437'

# Require the user to enter city
city = input("Please enter your city: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={key}'
extract = requests.get(url)
data = extract.json()
while True:
    if data['cod'] == "404":
        print('The city you entered was not found.')
        city = input("Please re-enter your city: ")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={key}'
        extract = requests.get(url)
        data = extract.json()
    else:
        print(f'Here is the weather data of {data["name"]}')
        print(f'Coordinate: {data["coord"]["lon"]} Long and {data["coord"]["lat"]} Lat')
        print(f'Temperature: {round(data["main"]["temp"]-273,2)} degC')
        print(f'Weather: {data["weather"][0]["main"]} with {data["weather"][0]["description"]}')
        print(f'Humidity Level: {data["main"]["humidity"]}%')
        print(f'Wind speed: {data["wind"]["speed"]}km/h')
        break