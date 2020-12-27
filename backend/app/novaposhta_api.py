# -*- encoding: utf-8 -*-

import requests
from .models import Order
import re

API_URL = 'https://api.novaposhta.ua/v2.0/json/'

NOVAPOSHTA_API_KEY = '0dfcb26f26a8b36a211887975c95d7fe'


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
					'Ref': warehouse['Ref'],
				})
	except requests.exceptions.HTTPError:
		pass

	return result


def invoice(order_id):
	order = Order.objects.get(id=order_id)
	recipient_name = '%s %s' % (order.customer_surname, order.customer_name)
	customer_phone = "".join(re.split('[()-]+', order.customer_phone))
	data = {
		"apiKey": NOVAPOSHTA_API_KEY,
		"modelName": "InternetDocument",
		"calledMethod": "save",
		"methodProperties": {
			"NewAddress": "1",
			"PayerType": "Recipient",
			"PaymentMethod": "Cash",
			"CargoType": "Cargo",
			"VolumeGeneral": "",
			"Weight": "5",
			"ServiceType": "WarehouseWarehouse",
			"SeatsAmount": "1",
			"Description": "одежда",
			"Cost": "1499",
			"CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
			"Sender": "78db64c2-9ad6-11e6-a54a-005056801333",
			"SenderAddress": "01ae25f4-e1c2-11e3-8c4a-0050568002cf",
			"ContactSender": "32a28604-cd6b-11e8-8b24-005056881c6b",
			"SendersPhone": "380507204066",
			"RecipientCityName": order.city,
			"RecipientArea": "",
			"RecipientAreaRegions": "",
			"RecipientAddressName": order.post_office_ref,
			"RecipientHouse": "",
			"RecipientFlat": "",
			"RecipientName": recipient_name,
			"RecipientType": "PrivatePerson",
			"RecipientsPhone": customer_phone,
			"BackwardDeliveryData": [
				{
					"PayerType": "Recipient",
					"CargoType": "Money",
					"RedeliveryString": "1499"
				}
			]
		}
	}
	success = False
	try:
		response = requests.post(API_URL, json=data)
		response_data = response.json()
		if response_data['success']:
			for el in response_data['data']:
				order.invoice_number = el['IntDocNumber']
				order.cost_on_site = el['CostOnSite']
			order.save()
			success = True
	except requests.exceptions.HTTPError:
		pass
	result = {
		'success': success,
		'response': response_data
	}
	return result


def get_errors():
	data = {
		"apiKey": NOVAPOSHTA_API_KEY,
		"modelName": "CommonGeneral",
		"calledMethod": "getMessageCodeText",
		"methodProperties": {}
	}
	error_codes = []
	try:
		response = requests.post(API_URL, json=data)
		response_data = response.json()
		if response_data['success']:
			for el in response_data['data']:
				error_codes.append(el)
	except requests.exceptions.HTTPError:
		pass
	return error_codes
