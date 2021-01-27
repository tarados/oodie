from django.urls import path
from .views import *

urlpatterns = [
	path('products', products),
	path('products/product/<int:product_id>', product),
	path('cities', novaposhta_api_city),
	path('warehouse', novaposhta_api_warehouse),
	path('order', order),
	path('report', report),
	path('locales', locales),
	path('invoice', novaposhta_api_invoice),
]
