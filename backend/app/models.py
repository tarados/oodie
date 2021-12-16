from django.db import models
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.conf import settings
from django.db.models.signals import post_save
from sorl.thumbnail import get_thumbnail
import logging
from .log import my_logger

my_logger()
log = logging.getLogger('my_logger')


class Localization(models.Model):
	key = models.CharField("Ключ текста", max_length=255, null=True, blank=True)
	value = models.TextField("Значение на русском", null=True, blank=True)
	value_ua = models.TextField("Значение на украинском", null=True, blank=True)
	# value_en = models.TextField("Значение на английском", null=True, blank=True)

	class Meta:
		verbose_name = "Локализация"
		verbose_name_plural = "Локализации"

	def __str__(self):
		return self.key


class Translates(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'название перевода')
	name_locale = models.ForeignKey(Localization, verbose_name=u'ключ для перевода', null=True, blank=True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Перевод"
		verbose_name_plural = "Переводы"

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'название категории')
	name_locale = models.ForeignKey(Localization, verbose_name=u'перевод категории', null=True, blank=True, on_delete=models.CASCADE, related_name='name_translate')
	category_description = models.ForeignKey(Localization, verbose_name=u'описание категории', null=True, blank=True, on_delete=models.CASCADE, related_name='category_description_translate')
	slug = models.SlugField(null=True)

	class Meta:
		verbose_name = u'категория'
		verbose_name_plural = u'категории'

	def __str__(self):
		return self.name


class Size(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'размер')

	class Meta:
		verbose_name = u'размер'
		verbose_name_plural = u'размеры'

	def __str__(self):
		return self.name


class TableOfSize(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='images/', verbose_name=u'Таблица размеров')

	class Meta:
		verbose_name = u'Таблица размеров'
		verbose_name_plural = u'Таблицы размеров'

	def __str__(self):
		return self.name


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name=u'название')
	title_locale = models.ForeignKey(Localization, verbose_name=u'перевод названия', null=True, blank=True, on_delete=models.CASCADE, related_name='title_translate')
	description = models.TextField(verbose_name=u'описание')
	description_locale = models.ForeignKey(Localization, verbose_name=u'перевод описания', null=True, blank=True, on_delete=models.CASCADE, related_name='description_translate')
	price = models.IntegerField(verbose_name=u'цена')
	new_price = models.IntegerField(verbose_name=u'новая цена', null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name=u'категория', null=True, on_delete=models.CASCADE)
	table = models.ForeignKey(TableOfSize, verbose_name=u'таблица размеров', null=True, blank=True,
							  on_delete=models.SET_NULL)
	hidden = models.BooleanField(verbose_name='снять с продажи', default=False)
	order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta:
		ordering = ['order']
		verbose_name = u'товар'
		verbose_name_plural = u'товары'

	def __str__(self):
		return self.title

	def get_first_image_url(self):
		try:
			first_image = ProductImage.objects.filter(product=self.id)[0].image
			im = get_thumbnail(first_image, '600x600', crop='center', quality=99)
			log.debug('get_first_image_url - %s' % (settings.SITE_URL + im.url))
			return settings.SITE_URL + im.url
		except IndexError:
			logging.exception("error")
			return None

	def get_price(self):
		try:
			if self.new_price:
				return self.new_price
			else:
				return self.price
		except IndexError:
			return self.price

	get_price.short_description = "Цена"

	def admin_description(self):
		max_len = 30
		result = self.description
		if len(result) > max_len:
			result = result[:max_len] + "..."
		return result

	admin_description.short_description = "Описание"

	def get_image(self):
		size = 50
		image_url = f'{settings.SITE_URL}{settings.STATIC_URL}no-img.jpg'
		try:
			obj = ProductImage.objects.filter(product=self.id)[0]
			image_url = obj.image.url
		except IndexError:
			pass
		return mark_safe(f'<img src="{image_url}" height="{size}"')

	get_image.short_description = "Первое изображение"

	def availability_dict(self):
		availabilities = ProductAvailability.objects.filter(product=self.id)
		availability_list = []
		for availability in availabilities:
			availability_list.append({
				'size': availability.size.name,
				'quantity': availability.quantity,
				'preorder': availability.preorder
			})
		log.debug("availability_dict - %s" % availability_list)
		return availability_list

	def availability_info(self):
		availabilities = ProductAvailability.objects.filter(product=self)
		availability_size_list = []
		for availability in availabilities:
			availability_size_list.append(
				'%s - %s' % (availability.size.name, availability.quantity)
			)
		return ', '.join(availability_size_list)

	availability_info.short_description = "Размеры в наличии"

	def get_table_of_size(self):
		if self.table_id:
			log.debug("get_table_of_size - %s" % (settings.SITE_URL + self.table.image.url))
			return settings.SITE_URL + self.table.image.url
		return None

	get_table_of_size.short_description = "Таблица размеров"


class ProductAvailability(models.Model):
	size = models.ForeignKey(Size, verbose_name=u'размер', null=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, verbose_name=u'название модели', null=True, on_delete=models.CASCADE)
	quantity = models.IntegerField(verbose_name='Количество', null=True)
	preorder = models.BooleanField(verbose_name='Предзаказ', default=False)

	class Meta:
		verbose_name = u'наличие товара'
		verbose_name_plural = u'наличие товаров'

	def __str__(self):
		product = Product(id=self.product).title
		return product


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='additional_image', on_delete=models.CASCADE,
								verbose_name='Название')
	image = models.ImageField(upload_to='images/', verbose_name=u'изображение')
	order = models.PositiveIntegerField(default=0, blank=False, null=False)

	class Meta:
		ordering = ['order']
		verbose_name = u'изображение товара'
		verbose_name_plural = u'изображения товара'

	def get_image(self):
		return mark_safe(f'<img src="%s" width="150" height="150"' % (self.image.url,))

	get_image.short_description = "Изображение"

	def __str__(self):
		return str(self.product)


class Order(models.Model):
	"""Модель Заказ"""

	STATUS_CHOICE = ((1, "Новый"),
					 (2, "В обработке"),
					 (3, "Выполнен"),
					 (4, "Предзаказ"),
					 (5, "Отменен"))
	STATUS_COLORS = ((1, "red"),
					 (2, "yellow"),
					 (3, "green"),
					 (4, "blue"),
					 (5, "grey"))
	date = models.DateTimeField("Дата", null=True, blank=True)
	total_price = models.FloatField("Сумма", null=True, blank=True)
	customer_name = models.CharField("Имя", max_length=20)
	customer_surname = models.CharField("Фамилия", max_length=20, null=True, blank=True)
	customer_phone = models.CharField("Телефон", max_length=20)
	delivery = models.CharField("Доставка", max_length=50, null=True, blank=True)
	payment = models.CharField("Оплата", max_length=50, null=True, blank=True)
	city = models.CharField("Город", max_length=255, null=True, blank=True)
	city_ref = models.CharField("Код города", max_length=255, null=True, blank=True)
	post_office_ref = models.CharField("Номер отделения", max_length=25, null=True, blank=True)
	post_office = models.TextField("Почтовое отделение", null=True, blank=True)
	address = models.TextField("Адрес доставки", null=True, blank=True)
	comment = models.TextField("Комментарий", null=True, blank=True)
	date_send = models.DateField("Дата отправки", null=True, blank=True)
	invoice_number = models.CharField("Номер накладной", max_length=250, null=True, blank=True)
	cost_on_site = models.CharField("Стоимость доставки, грн.", max_length=10, null=True, blank=True)
	status = models.IntegerField("Статус", choices=STATUS_CHOICE, default=1)
	preorder = models.BooleanField(verbose_name='Предзаказ', default=False)

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def total_price_calc(self):
		products = list(OrderItem.objects.filter(order=self.id))
		total_price = 0
		for product in products:
			total_price = total_price + product.cost_product_calc()
		return total_price

	total_price_calc.short_description = "Сумма"

	def save(self):
		order_items = OrderItem.objects.filter(order=self.id)
		availabilities = ProductAvailability.objects.all()
		if self.status == 3:
			for order_item in order_items:
				availability = availabilities.get(product=order_item.product, size=order_item.size)
				availability.quantity = availability.quantity - order_item.quantity
				availability.save()
		super().save()

	def delete(self):
		order_items = OrderItem.objects.filter(order=self.id)
		availabilities = ProductAvailability.objects.all()
		for order_item in order_items:
			availability = availabilities.get(product=order_item.product, size=order_item.size)
			availability.quantity = availability.quantity + order_item.quantity
			availability.save()

	def __str__(self):
		return '№ %s' % str(self.id)


class OrderItem(models.Model):
	"""Модель Контент заказа"""

	order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	price = models.FloatField("Цена", null=True, blank=True)
	quantity = models.FloatField("Количество", null=True, blank=True)
	cost_product = models.FloatField("Сумма", null=True, blank=True)
	size = models.ForeignKey(Size, verbose_name=u'размер', null=True, on_delete=models.SET_NULL)
	preorder = models.BooleanField(verbose_name='Предзаказ', default=False)

	class Meta:
		verbose_name = "Контент заказа"
		verbose_name_plural = "Контент заказов"

	def cost_product_calc(self):
		return self.price * self.quantity

	def __str__(self):
		return 'Заказ № %s для %s' % (self.order.id, self.order.customer_name)


@receiver(post_save, sender=OrderItem)
def update_calculated_fields(sender, instance, **kwargs):
	cost_product = instance.cost_product_calc()
	instance_id = str(instance.order).split(' ')[1]
	order = Order.objects.get(id=instance_id)
	order.preorder = instance.preorder
	order.save()
	sender.objects.filter(pk=instance.pk).update(cost_product=cost_product)
