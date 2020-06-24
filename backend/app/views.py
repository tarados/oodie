from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductImage, Product


def products(request):
	products_list = []
	all_products = Product.objects.all()
	for prd in all_products:
		products_list.append(
			{
				'title': prd.title,
				'price': prd.price,
				'old_price': prd.old_price,
				'image': ProductImage.objects.filter(product=prd.id)[0].image.url
			}
		)
	return JsonResponse({'products': products_list})


def product(request, product_id):
	prd = Product.objects.get(id=int(product_id))
	product_case = {
		'title': prd.title,
		'price': prd.price,
		'old_price': prd.old_price,
		'description': prd.description,
		'image': ProductImage.objects.filter(product=prd.id)[0].image.url
	}
	return JsonResponse({'product': product_case})
