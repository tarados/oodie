from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'category', 'get_image', 'description', )
	inlines = [
		ProductImageInline,
	]


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	list_display = (
		"idOrder", "date", "total_price", "customer_name", "customer_surname", "customer_phone", "status")
	list_filter = ("status",)
	inlines = [
		OrderItemInline,
	]

	def idOrder(self, obj):
		return 'Заказ № %s' % str(obj.id)

	idOrder.short_description = "Номер заказа"

	def save_model(self, request, obj, form, change):
		obj.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.site_title = "Oodie"
admin.site.site_header = "Oodie"
