import logging
import json
import requests

LOGGER = logging.getLogger(__name__)


def print_response(response: requests.Response):
    # request
    print("\nSend {} {} HTTP {}".format(response.request.method, response.url, response.status_code))
    print("Request headers: \n{}".format(response.request.headers))
    print("Request body: {}".format(response.request.body))

    # response
    print("Response body: {}".format(response.text))

def get_json(f_name):
    f = open(f_name)
    pet_json = json.load(f)
    return pet_json
