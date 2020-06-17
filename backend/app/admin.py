from django.contrib import admin
from .models import Category, Product, ProductImage
from django.utils.safestring import mark_safe


class ProductImageAdmin(admin.ModelAdmin):
	list_display = ('product', 'get_image')

	def get_image(self, obj):
		return mark_safe(f'<img src="%s" width="150" height="150"' % (obj.image.url,))

	get_image.short_description = "Изображение"


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price')
	inlines = [
		ProductImageInline,
	]


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.site_title = "Oodie"
admin.site.site_header = "Oodie"
