# -*- encoding: utf-8 -*-

import requests
from .models import Order

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
				result.append({
					'warehouse': warehouse['DescriptionRu'],
					'warehouseRef': warehouse['Number'],
				})
	except requests.exceptions.HTTPError:
		pass

	return result


def invoice(order_id):
	order = Order.objects.get(id=order_id)
	recipient_name = '%s %s' % (order.customer_surname, order.customer_name)
	date_send = order.date_send
	data = {
		"apiKey": "cd0fe6f50623590fa01e0ad0a88aaaad",
		"modelName": "InternetDocument",
		"calledMethod": "save",
		"methodProperties": {
			"NewAddress": "1",
			"PayerType": "Sender",
			"PaymentMethod": "Cash",
			"CargoType": "Cargo",
			"VolumeGeneral": "0.1",
			"Weight": "10",
			"ServiceType": "WarehouseWarehouse",
			"SeatsAmount": "1",
			"Description": "абажур",
			"Cost": "500",
			"CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
			"Sender": "10e048ed-e089-11ea-8513-b88303659df5",
			"SenderAddress": "00000000-0000-0000-0000-000000000000",
			"ContactSender": "1fcf8db1-e089-11ea-8513-b88303659df5",
			"SendersPhone": "380991234567",
			"RecipientCityName": "Львів",
			"RecipientArea": "",
			"RecipientAreaRegions": "",
			"RecipientAddressName": "2",
			"RecipientHouse": "",
			"RecipientFlat": "",
			"RecipientName": "Драгунов Ігор Євгенович",
			"RecipientType": "PrivatePerson",
			"RecipientsPhone": "380991234567",
			"DateTime": "04.12.2020"
		}
	}
	try:
		response = requests.post(API_URL, json=data)
		response_data = response.json()
		print(response_data)
		if response_data['success']:
			for el in response_data['data']:
				order.invoice_number = el['IntDocNumber']
				order.cost = el['CostOnSite']
	except requests.exceptions.HTTPError:
		pass
	order.save()
	# return result