import requests


def get_api_data(api_endpoint: str):
    r = requests.get(api_endpoint)
    return r.json()['results']
