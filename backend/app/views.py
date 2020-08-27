import os
import json
import datetime
from django.shortcuts import render
from app import novaposhta_api
from django.http import JsonResponse, HttpResponse
from .models import ProductImage, Product, Order, OrderItem, Category



def products(request):
	products_list = []
	categories_list = []
	all_products = Product.objects.all()
	all_categories = Category.objects.all()
	for category in all_categories:
		categories_list.append({
			'id': category.id,
			'title': category.name,
			'slug': category.slug
		})
	for prod in all_products:
		if prod.hidden:
			pass
		else:
			products_list.append(
				{
					'id': prod.id,
					'title': prod.title,
					'category': prod.category_id,
					'price': prod.price,
					'new_price': prod.new_price,
					'image': os.environ['SITE_URL'] + ProductImage.objects.filter(product=prod.id)[0].image.url
				}
			)
	return JsonResponse({'products': products_list, 'categories': categories_list})


def product(request, product_id):
	prod = Product.objects.get(id=int(product_id))
	images_url = []
	for image in ProductImage.objects.filter(product=prod.id):
		images_url.append(os.environ['SITE_URL'] + image.image.url)
	product_case = {
		'id': prod.id,
		'title': prod.title,
		'price': prod.price,
		'new_price': prod.new_price,
		'description': prod.description,
		'image_list': images_url
	}
	return JsonResponse({'product': product_case})


def order(request):
	order_str = request.body.decode()
	order_content = json.loads(order_str)
	print(order_content)
	order = Order(
		date=datetime.datetime.now(),
		customer_name=order_content["username"],
		customer_phone=order_content["phone"],
		delivery=order_content["delivery"],
		city=order_content["city"],
		post_office=order_content["warehouse"],
		address=order_content["others"]
	)
	order.save()
	order_total_sum = 0
	for order_item in order_content["products"]:
		product = Product.objects.get(id=int(order_item["id"]))
		current_price = product.price
		if current_price >= order_item["price"]:
			product_price = current_price
		else:
			product_price = order_item["price"]
		order_item = OrderItem(
			order=order,
			product=product,
			quantity=order_item["quantity"],
			price=product_price,
			cost_product=product_price * order_item["quantity"]
		)
		order_item.save()
		order_total_sum = order_total_sum + order_item.cost_product
	order.total_price = order_total_sum
	order.save()
	return JsonResponse({'success': True})


def novaposhta_api_city(request):
    name = request.GET.get('name', '')
    result = novaposhta_api.get_city(name)
    return HttpResponse(json.dumps(result), content_type='application/json')


def novaposhta_api_warehouse(request):
    city_id = request.GET.get('city_id', None)
    if city_id is None:
        result = []
    else:
        name = request.GET.get('name', '')
        result = novaposhta_api.get_warehouses(city_id, name)
    return HttpResponse(json.dumps(result), content_type='application/json')