import requests
import json_samp.json_var as jv
from api.utils import print_response

def send_post_pet(host: str, pet_json: dict) -> requests.Response:
    r = requests.post(url=host + '/pet', json=pet_json)
    print_response(r)
    return r

def send_get_pet(host: str, pet_id: int) -> requests.Response:
    r = requests.get(url=host + '/pet/' + str(pet_id))
    print_response(r)
    return r

def send_del_pet(host: str, pet_id: int) -> requests.Response:
    r = requests.delete(url=host + '/pet/' + str(pet_id))
    print_response(r)
    return r