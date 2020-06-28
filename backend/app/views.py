from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductImage, Product
import os


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