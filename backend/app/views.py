from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductImage, Product, Order, OrderItem
import os
import json
import datetime


def products(request):
	products_list = []
	all_products = Product.objects.all()
	for prd in all_products:
		products_list.append(
			{
				'id': prd.id,
				'title': prd.title,
				'price': prd.price,
				'new_price': prd.new_price,
				'image': os.environ['SITE_URL'] + ProductImage.objects.filter(product=prd.id)[0].image.url
			}
		)
	return JsonResponse({'products': products_list})


def product(request, product_id):
	prd = Product.objects.get(id=int(product_id))
	images_url = []
	for image in ProductImage.objects.filter(product=prd.id):
		images_url.append(os.environ['SITE_URL'] + image.image.url)
	product_case = {
		'id': prd.id,
		'title': prd.title,
		'price': prd.price,
		'new_price': prd.new_price,
		'description': prd.description,
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
		post_office=order_content["post-office"],
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