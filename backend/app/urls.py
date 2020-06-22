from django.urls import path
from .views import *

urlpatterns = [
	path('products', products),
	path('products/product/<int:product_id>', product),
]