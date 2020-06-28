from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'category', 'get_image', 'description', )
	inlines = [
		ProductImageInline,
	]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.site_title = "Oodie"
admin.site.site_header = "Oodie"
