import requests
from api.utils import print_response

# Request to add a pet
def send_post_pet(host: str, pet_json: dict) -> requests.Response:
    r = requests.post(url=host + '/pet', json=pet_json)
    print_response(r)
    return r

# Request for information about a pet by id
def send_get_pet(host: str, pet_id: int) -> requests.Response:
    r = requests.get(url=host + '/pet/' + str(pet_id))
    print_response(r)
    return r

# Request to remove a pet by id
def send_del_pet(host: str, pet_id: int) -> requests.Response:
    r = requests.delete(url=host + '/pet/' + str(pet_id))
    print_response(r)
    return r