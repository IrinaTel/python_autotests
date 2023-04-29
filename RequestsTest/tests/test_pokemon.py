import requests
import pytest

def test_status_code():
    token = "0f8707830425904346c58ecb126e9eec"
    base_url = "https://pokemonbattle.me:9104/"
    response = requests.get(f'{base_url}trainers')
    assert response.status_code ==200


def test_part_of_json():
    token = "0f8707830425904346c58ecb126e9eec"
    base_url = "https://pokemonbattle.me:9104/"
    response = requests.get(f'{base_url}trainers', params={"trainer_id": "4180"})  
    assert response.json()["trainer_name"] == "PyTrainer"

