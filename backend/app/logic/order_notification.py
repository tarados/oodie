from django.conf import settings

from .email import send_email_template


def send_order_notification(order):
    delivery_list = [order.delivery]
    if order.city:
        delivery_list.append(order.city)
    if order.post_office:
        delivery_list.append(order.post_office)

    delivery = ", ".join(delivery_list)

    products = list()
    order_items = list(order.item.all())
    for item in order_items:
        products.append({
            'name': item.product.title,
            'quantity': int(item.quantity),
            'size': item.size.name,
            'price': int(item.cost_product),
        })

    send_email_template(settings.ADMIN_EMAILS, "Новый Заказ", "order_email.html", {
        'order_id': order.id,
        'customer_name': f'{order.customer_name} {order.customer_surname}',
        'customer_phone': order.customer_phone,
        'delivery': delivery,
        'payment': order.payment,
        'comment': order.comment,
        'total_price': order.total_price,
        'products': products,
    })
