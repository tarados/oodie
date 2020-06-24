from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Product, ProductImage
from django.utils.safestring import mark_safe


# class ProductImageAdmin(admin.ModelAdmin):
# 	list_display = ('product', 'get_image')
# 	list_filter = ('product',)
#
# 	def get_image(self, obj):
# 		return mark_safe(f'<img src="%s" width="150" height="150"' % (obj.image.url,))
#
# 	get_image.short_description = "Изображение"


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 3


class ProductAdmin(admin.ModelAdmin):
	inlines = [
		ProductImageInline,
	]


# admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.site_title = "Oodie"
admin.site.site_header = "Oodie"
