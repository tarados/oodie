from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductImage, Product


def products(request):
	products_list = []
	products = Product.objects.all()
	for product in products:
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
