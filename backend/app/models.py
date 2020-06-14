from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'название')

	class Meta:
		verbose_name = u'категория'
		verbose_name_plural = u'категории'

	def __unicode__(self):
		return self.name


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name=u'название')
	description = models.TextField(verbose_name=u'описание')
	price = models.IntegerField(verbose_name=u'цена')
	old_price = models.IntegerField(verbose_name=u'старая цена', null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name=u'категория', null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.title


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='additional_image', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/', verbose_name=u'изображение')

	class Meta:
		verbose_name = u'изображение товара'
		verbose_name_plural = u'изображения товара'

	def __unicode__(self):
		return ''
