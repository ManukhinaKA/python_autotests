import requests

# Переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eee02a1452a45fab93918fcdf61d37a2'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}

# Боди
create_BODY = {
    "name": "Fox",
    "photo_id": 831
}


# Создать покемона
create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_BODY)
print(f'Статус код {create.status_code}. Сообщение: {create.json()["message"]}')
create_json = create.json()
key_id_pokemon = create_json["id"] 

# Поймать покемона в покебол
pokebody = {
    "pokemon_id": create_json["id"]
} 

add_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokebody)
print(f'Статус код {add_pockeball.status_code}. Сообщение: {add_pockeball.json()["message"]}')

# Изменить покемона
change_BODY = {
    "pokemon_id": create_json["id"],
    "name": "Имбирь",
    "photo_id": 831
}

change_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_BODY)
print(f'Статус код {change_pokemon.status_code}. Сообщение: {change_pokemon.json()["message"]}')

