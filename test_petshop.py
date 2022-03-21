import pytest
from api.http_methods import send_post_pet, send_get_pet, send_del_pet
from api.utils import get_json
import json

PETSHOP_URL = "https://petstore3.swagger.io/api/v3"
JSON_NAME = "pet.json"
PET_ID = 123

def test_post():
    pet_json = get_json(JSON_NAME)
    response = send_post_pet(PETSHOP_URL, pet_json)
    assert response.status_code == 200

def test_get():
    response = send_get_pet(PETSHOP_URL, PET_ID)
    assert response.status_code == 200

def test_delete():
    response = send_del_pet(PETSHOP_URL, PET_ID)
    assert response.status_code == 200