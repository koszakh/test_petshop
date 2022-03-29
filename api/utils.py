import json
import requests
import json_var as jv

# Displaying information about a request
def print_response(response: requests.Response):
    # request
    print("\nSend {} {} HTTP {}".format(response.request.method, response.url, response.status_code))
    print("Request headers: \n{}".format(response.request.headers))
    print("Request body: {}".format(response.request.body))

    # response
    print("Response body: {}".format(response.text))

# Get data from a json-file
def get_json(f_name: str) -> dict:
    f = open(f_name)
    pet_json = json.load(f)
    return pet_json

# Get dict data from a python file
def get_var_json() -> dict:
    return jv.dct

def get_req_pet_name(response: requests.Response) -> str:
    body_dict = json.loads(response.request.body)
    pet_name = body_dict.get("name")
    return pet_name

def get_resp_pet_name(response: requests.Response) -> str:
    body_dict = json.loads(response.text)
    pet_name = body_dict.get("name")
    return pet_name