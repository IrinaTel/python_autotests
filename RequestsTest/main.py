import requests

token = "0f8707830425904346c58ecb126e9eec"
base_url = "https://pokemonbattle.me:9104/"


#создаю покемона
response_creating_pokemon = requests.post(f'{base_url}pokemons', headers={"trainer_token": token}, json=
    {
    "name": "кулебяка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_creating_pokemon.text)

pokemon_id = response_creating_pokemon.json()['id'] #пихаю id покемона в переменную, чтобы потом передать его в запросе на изменение имени
print(str(pokemon_id))
print(f'"{pokemon_id}"')

#меняю имя созданного покемона

response_change_name = requests.put(f'{base_url}pokemons', headers={"trainer_token": token},json = {
    "pokemon_id": "9693",
    "name": "New кулебка",
})

print(response_change_name.text)


response_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={"trainer_token":token}, json = {
    "pokemon_id": "9693"
})

print(response_pokeball.text)