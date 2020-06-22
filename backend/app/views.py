from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductImage, Product


def products(request):
	products_list = []
	all_products = Product.objects.all()
	for product in all_products:
		products_list.append(
			{
				'title': product.title,
				'price': product.price,
				'old_price': product.old_price,
				'description': product.description,
				'image': ProductImage.objects.get(product=product.id).image.url
			}
		)
	return JsonResponse({'products': products_list})


def product(request, product_id):
	select_product = Product.objects.get(id=int(product_id))
	product_case = {
		'title': select_product.title,
		'price': select_product.price,
		'old_price': select_product.old_price,
		'description': select_product.description,
		'image': ProductImage.objects.get(product=product_id).image.url
	}
	return JsonResponse({'product': product_case})
