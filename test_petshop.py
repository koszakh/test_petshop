import pytest
from api.http_methods import send_post_pet, send_get_pet, send_del_pet
from api.utils import get_json, get_var_json, get_req_pet_name, get_resp_pet_name
import variables as var

petshopUrl = var.PETSHOP_URL
jsonName = var.JSON_NAME
petId = var.PET_ID

# Testing adding a pet
def test_post():
    pet_json = get_json(jsonName)
    response = send_post_pet(petshopUrl, pet_json)
    assert response.status_code == 200

# Testing adding a pet with variables
def test_post_var():
    pet_json = get_var_json()
    response = send_post_pet(petshopUrl, pet_json)
    assert response.status_code == 200

# Testing getting data about a pet by id
def test_get():
    response = send_get_pet(petshopUrl, petId)
    assert response.status_code == 200

# Testing deleting pet data by number
def test_delete():
    response = send_del_pet(petshopUrl, petId)
    assert response.status_code == 200

# Testing the functionality of the pet store
def test_petshop():
    pet_json = get_var_json()
    resp_post = send_post_pet(petshopUrl, pet_json)
    assert resp_post.status_code == 200
    pet_name_post = get_req_pet_name(resp_post)

    pet_id = resp_post.json().get('id')
    resp_get = send_get_pet(petshopUrl, pet_id)
    pet_name_get = get_resp_pet_name(resp_get)
    assert resp_get.status_code == 200
    assert pet_name_post == pet_name_get

    resp_del = send_del_pet(petshopUrl, pet_id)
    assert resp_del.status_code == 200
    assert resp_del.text == "Pet deleted"

    resp_get_del = send_get_pet(petshopUrl, pet_id)
    assert resp_get_del.status_code == 404