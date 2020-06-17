from django.contrib import admin
from .models import Category, Product, ProductImage
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title',)


class ProductImageAdmin(admin.ModelAdmin):
	list_display = ('product', 'image', 'get_image')

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

	get_image.short_description = "Изображение"


admin.site.register(Category)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.site_title = "Oodie"
admin.site.site_header = "Oodie"

