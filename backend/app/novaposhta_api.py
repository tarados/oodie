# -*- encoding: utf-8 -*-

import requests


API_URL = 'https://api.novaposhta.ua/v2.0/json/'

NOVAPOSHTA_API_KEY = 'cd0fe6f50623590fa01e0ad0a88aaaad'


def get_city(name=None):
    data = {
        'modelName': 'Address',
        'calledMethod': 'getCities',
        'apiKey': NOVAPOSHTA_API_KEY
    }
    if name is not None:
        data['methodProperties'] = {'FindByString': name}

    result = []

    try:
        response = requests.post(API_URL, json=data)
        response_data = response.json()

        if response_data['success']:
            for city in response_data['data']:
                result.append({
                    'id': city['Ref'],
                    'name': city['DescriptionRu']})
    except requests.exceptions.HTTPError:
        pass

    return result


def get_warehouses(city_id, name):
    data = {
        'modelName': 'Address',
        'calledMethod': 'getWarehouses',
        'apiKey': NOVAPOSHTA_API_KEY,
        'methodProperties': {
            'CityRef': city_id,
        }
    }
    if name is not None:
        data['methodProperties']['FindByString'] = name

    result = []

    try:
        response = requests.post(API_URL, json=data)
        response_data = response.json()

        if response_data['success']:
            for warehouse in response_data['data']:
                result.append(warehouse['DescriptionRu'])
    except requests.exceptions.HTTPError:
        pass

    return result




