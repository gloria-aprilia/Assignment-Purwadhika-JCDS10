import requests

while True:
    try: 
        name = input("Please enter a valid pokemon name: ")
        while True:
            if name.isalpha() == True:
                url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
                ext = requests.get(url)
                data = ext.json()
                break
            else:
                print("Name you entered was not found.")
                name = input("Please enter a valid pokemon name: ")
        break
    except:
        print("Name you entered was not found.")

print(f"----- {data['name']} (ID: {data['id']}) -----")
print(f"HP = {data['stats'][0]['base_stat']}")
print(f"Attack = {data['stats'][1]['base_stat']}")
print(f"Defense = {data['stats'][2]['base_stat']}")
print(f"Speed = {data['stats'][-1]['base_stat']}")
print(f"Type = {data['types'][0]['type']['name']}")
print(f"Image = {data['sprites']['front_default']}")
print("Abilities = ")
for i in range(len(data['abilities'])):
    print(f"{i+1}. {data['abilities'][i]['ability']['name'].capitalize()}")