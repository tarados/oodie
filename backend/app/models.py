from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'название')

	class Meta:
		verbose_name = u'категория'
		verbose_name_plural = u'категории'

	def __str__(self):
		return self.name


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name=u'название')
	description = models.TextField(verbose_name=u'описание')
	price = models.IntegerField(verbose_name=u'цена')
	new_price = models.IntegerField(verbose_name=u'старая цена', null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name=u'категория', null=True, on_delete=models.CASCADE)

	class Meta:
		verbose_name = u'товар'
		verbose_name_plural = u'товары'

	def get_image(self):
		obj = ProductImage.objects.filter(product=self.id)[0]
		return mark_safe(f'<img src="%s" width="150" height="150"' % (obj.image.url,))

	get_image.short_description = "Первое изображение"

	def __str__(self):
		return self.title


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='additional_image', on_delete=models.CASCADE, verbose_name='Название')
	image = models.ImageField(upload_to='images/', verbose_name=u'изображение')

	class Meta:
		verbose_name = u'изображение товара'
		verbose_name_plural = u'изображения товара'

	def get_image(self):
		return mark_safe(f'<img src="%s" width="150" height="150"' % (self.image.url,))

	get_image.short_description = "Изображение"

	def __str__(self):
		return str(self.product)
