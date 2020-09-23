from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'название')
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


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name=u'название')
	description = models.TextField(verbose_name=u'описание')
	price = models.IntegerField(verbose_name=u'цена')
	new_price = models.IntegerField(verbose_name=u'новая цена', null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name=u'категория', null=True, on_delete=models.CASCADE)
	hidden = models.BooleanField(verbose_name='снять с продажи', default=False)

	class Meta:
		verbose_name = u'товар'
		verbose_name_plural = u'товары'

	def get_price(self):
		try:
			if self.new_price:
				return self.new_price
			else:
				return self.price
		except IndexError:
			return self.price

	get_price.short_description = "Цена"

	def get_image(self):
		try:
			obj = ProductImage.objects.filter(product=self.id)[0]
			return mark_safe(f'<img src="%s" width="150" height="150"' % (obj.image.url,))
		except IndexError:
			image_url = settings.SITE_URL + settings.STATIC_URL + 'no-img.jpg'
			return mark_safe(f'<img src="%s" width="150" height="150"' % image_url)

	get_image.short_description = "Первое изображение"

	def __str__(self):
		return self.title

	def availability_dict(self):
		availabilities = ProductAvailability.objects.filter(product=self)
		availability_list = []
		for availability in availabilities:
			availability_list.append({
				'size': availability.size.name,
				'quantity': availability.quantity
			})
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


class ProductAvailability(models.Model):
	size = models.ForeignKey(Size, verbose_name=u'размер', null=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, verbose_name=u'название модели', null=True, on_delete=models.CASCADE)
	quantity = models.CharField(max_length=10, verbose_name='Количество', null=True)

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

	class Meta:
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
					 (3, "Выполнен"))
	date = models.DateTimeField("Дата заказа", null=True, blank=True)
	total_price = models.FloatField("Сумма заказа", null=True, blank=True)
	customer_name = models.CharField("Имя и фамилия", max_length=12)
	customer_phone = models.CharField("Телефон", max_length=20)
	delivery = models.CharField("Способ доставки", max_length=50, null=True, blank=True)
	city = models.CharField("Город", max_length=20, null=True, blank=True)
	post_office = models.CharField("Почтовое отделение", max_length=250, null=True, blank=True)
	address = models.CharField("Адрес доставки", max_length=250, null=True, blank=True)
	comment = models.CharField("Комментарий", max_length=250, null=True, blank=True)
	status = models.IntegerField("Статус", choices=STATUS_CHOICE, default=1)

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def __str__(self):
		return 'Заказ № %s' % str(self.id)


class OrderItem(models.Model):
	"""Модель Контент заказа"""

	order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	price = models.FloatField("Цена", null=True, blank=True)
	quantity = models.FloatField("Количество", null=True, blank=True)
	cost_product = models.FloatField("Сумма", null=True, blank=True)

	class Meta:
		verbose_name = "Контент заказа"
		verbose_name_plural = "Контент заказов"

	def __str__(self):
		return 'Заказ № %s для %s' % (self.order.id, self.order.customer_name)
