from django.urls import path
from .views import *

urlpatterns = [
	path('products', products),
	path('products/product/<int:product_id>', product),
	path('novaposhta/city', novaposhta_api_city),
	path('novaposhta/warehouse', novaposhta_api_warehouse),
	path('order', order),
]