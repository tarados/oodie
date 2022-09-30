# -*- coding: utf-8 -*-
import os
import json
import datetime
import logging
from itertools import groupby
from django.conf import settings
from django.contrib import messages
from .logic.order_notification import send_order_notification
from .novaposhta_api import *
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from .models import ProductImage, Product, Order, OrderItem, Category, ProductAvailability, Size, Localization
from .novaposhta_api import invoice, get_errors
from .insta_parse import parse_insta
from .log import my_logger

my_logger()
log = logging.getLogger('my_logger')


def products(request):
    logging.info('start products request')
    products_list = []
    all_products = Product.objects.filter(hidden=False)
    log.info('iterate products')
    for prod in all_products:
        if prod.title_locale is None:
            title_translate = None
        else:
            title_translate = str(prod.title_locale)
        log.debug('product - %s' % {
            'id': prod.id,
            'title': prod.title,
            'title_translate': title_translate,
            'category': prod.category_id,
            'availability': prod.availability_dict(),
            'table': prod.get_table_of_size(),
            'price': prod.price,
            'new_price': prod.new_price,
            'image': prod.get_first_image_url()
        })
        products_list.append(
            {
                'id': prod.id,
                'title': prod.title,
                'title_translate': title_translate,
                'category': prod.category_id,
                'availability': prod.availability_dict(),
                'table': prod.get_table_of_size(),
                'price': prod.price,
                'new_price': prod.new_price,
                'image': prod.get_first_image_url()
            }
        )
    logging.info('end products request')

    return JsonResponse({
        'products': products_list,
    })


def product(request, product_id):
    prod = Product.objects.get(id=int(product_id))
    images_url = []
    for image in ProductImage.objects.filter(product=prod.id):
        images_url.append(os.environ['SITE_URL'] + image.image.url)
    if prod.title_locale is None:
        title_translate = None
    else:
        title_translate = str(prod.title_locale)
    if prod.description_locale is None:
        description_locale = None
    else:
        description_locale = str(prod.description_locale)
    product_case = {
        'id': prod.id,
        'title': prod.title,
        'title_translate': title_translate,
        'price': prod.price,
        'category': prod.category_id,
        'availability': prod.availability_dict(),
        'table': prod.get_table_of_size(),
        'new_price': prod.new_price,
        'description': prod.description,
        'description_locale': description_locale,
        'image_list': images_url
    }
    return JsonResponse({'product': product_case})


def categories(request):
    logging.info('start categories request')
    category_id = request.GET.get('category_id', None)
    categories_list = []
    all_categories = list(Category.objects.all())
    log.info('get categories from db - len_all_categories - %s' % len(all_categories))
    log.info('iterate categories')
    for category in all_categories:
        if category.name_locale is None:
            name_translate = None
        else:
            name_translate = str(category.name_locale)

        if category.category_description is None:
            category_description_locale = None
        else:
            category_description_locale = str(category.category_description)
        categories_list.append({
            'id': category.id,
            'title': category.name,
            'title_translate': name_translate,
            'category_description_locale': category_description_locale,
            'category_description': category.description,
            'slug': category.slug
        })

    logging.info('end categories request')

    return JsonResponse({
        'categories': categories_list
    })


def category(request, category_id):
    ctg = Category.objects.get(id=int(category_id))

    if ctg.name_locale is None:
        name_locale = None
    else:
        name_locale = str(ctg.name_locale)
    if ctg.category_description is None:
        description_locale = None
    else:
        description_locale = str(ctg.category_description)
    category_case = {
        'id': ctg.id,
        'title': ctg.name,
        'title_translate': name_locale,
        'description': ctg.description,
        'description_locale': description_locale
    }
    return JsonResponse({'category': category_case})


@transaction.atomic
def order(request):
    order_str = request.body.decode()
    order_content = json.loads(order_str)
    # print(order_content)

    order = Order(
        date=datetime.datetime.now(),
        customer_name=order_content["username"],
        customer_surname=order_content["userSurname"],
        customer_phone=order_content["phone"],
        delivery=order_content["delivery"],
        payment=order_content["payment"],
        city=order_content["city"],
        city_ref=order_content["city-ref"],
        post_office_ref=order_content["post-office-ref"],
        post_office=order_content["post-office"],
        address=order_content["others"],
        comment=order_content["comment"]
    )
    order.save()

    order_total_sum = 0
    preorder = False
    for order_item in order_content["products"]:
        product = Product.objects.get(id=int(order_item["id"]))
        if product.new_price is not None:
            price = product.new_price
        else:
            price = product.price
        size = Size.objects.get(name=order_item['size'])
        order_item = OrderItem(
            order=order,
            product=product,
            quantity=order_item["quantity"],
            price=price,
            size=size,
            preorder=order_item["preorder"],
            cost_product=order_item["price"] * order_item["quantity"]
        )
        if order_item.preorder:
            preorder = order_item.preorder
        order_item.save()
        order_total_sum = order_total_sum + order_item.cost_product
    order.total_price = order_total_sum
    order.preorder = preorder
    order.save()

    if not settings.DEBUG:
        send_order_notification(order)

    return JsonResponse({'success': True})


def novaposhta_api_city(request):
    name = request.GET.get('name', '')
    result = get_city(name)
    return HttpResponse(json.dumps(result), content_type='application/json')


def novaposhta_api_warehouse(request):
    city_id = request.GET.get('city_id', None)
    if city_id is None:
        result = []
    else:
        name = request.GET.get('name', '')
        result = get_warehouses(city_id, name)
    return HttpResponse(json.dumps(result), content_type='application/json')


def report(request):
    orders_list = list(Order.objects.filter(status="3"))
    sales = []
    for el in orders_list:
        order_items = OrderItem.objects.filter(order=el.id)
        for order_item in order_items:
            if order_item.product is None:
                continue
            sales.append({
                'name': order_item.product.title,
                'quantity': order_item.quantity
            })
    sales = sorted(sales, key=lambda x: x['name'])
    products_sale = {}
    for group in groupby(sales, key=lambda x: x['name']):
        name = group[0]
        items = group[1]
        item_quantity = 0
        for item in items:
            item_quantity += item['quantity']
        products_sale.update({
            name: item_quantity
        })
    return JsonResponse(products_sale)


def novaposhta_api_invoice(request):
    order_id = int(request.GET.get('order_id', ''))
    result = invoice(order_id)
    if not result['success']:
        errors_text = []
        list_errors = list(get_errors())
        for el in result['response']['errorCodes']:
            for error in list_errors:
                if el == error['MessageCode']:
                    if error['MessageDescriptionRU'] is not None:
                        errors_text.append(error['MessageDescriptionRU'])
                    else:
                        errors_text.append(error['MessageText'])
        message = ', '.join(errors_text)
        messages.error(request, message)
    return JsonResponse({'success': True})


def locales(request):
    localizations = Localization.objects.all()
    locale = {}
    key_ru = {}
    key_ua = {}
    for el in localizations:
        key_ru.update({el.key: el.value})
        key_ua.update({el.key: el.value_ua})
    locale.update({
        'ru-RU': key_ru,
        'uk-UA': key_ua
    })
    return JsonResponse(locale)
