from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
	path('products', products),
	path('categories', categories),
	path('products/product/<int:product_id>', product),
	path('categories/category/<int:category_id>', category),
	path('cities', novaposhta_api_city),
	path('warehouse', novaposhta_api_warehouse),
	path('order', order),
	path('report', report),
	path('locales', locales),
	path('invoice', novaposhta_api_invoice),
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
