import requests
import pytest

 #Базовые переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eee02a1452a45fab93918fcdf61d37a2'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}
trainer_ID = '5067'

#
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200 

def test_answer():
    response_answer = requests.get(url = f'{URL}/trainers', params = {'trainer_id': trainer_ID})
    assert response_answer.json()["data"][0]["id"] == "5067"
