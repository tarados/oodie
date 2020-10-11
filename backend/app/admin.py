from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem, Size, ProductAvailability, TableOfSize
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib.admin.templatetags.admin_modify import register, submit_row as original_submit_row


@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
	''' submit buttons context change '''
	ctx = original_submit_row(context)
	ctx.update({
		'show_save_and_add_another': context.get('show_save_and_add_another', ctx['show_save_and_add_another']),
		'show_save_and_continue': context.get('show_save_and_continue', ctx['show_save_and_continue']),
		'show_save': context.get('show_save', ctx['show_save']),
		'show_delete_link': context.get('show_delete_link', ctx['show_delete_link'])
	})
	return ctx


class ProductImageInline(SortableInlineAdminMixin, admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAvailabilityInline(admin.TabularInline):
	model = ProductAvailability
	extra = 0


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ('title', 'get_price', 'category', 'get_image', 'admin_description', 'hidden', 'availability_info')
	list_filter = ['category']
	list_editable = ['hidden']
	inlines = [
		ProductImageInline,
		ProductAvailabilityInline
	]

	def has_add_permission(cls, request):
		''' remove add and save and add another button '''
		return True

	def change_view(self, request, object_id, extra_context=None):
		''' customize add/edit form '''
		extra_context = extra_context or {}
		extra_context['show_save_and_continue'] = False
		extra_context['show_save'] = True
		return super(ProductAdmin, self).change_view(request, object_id, extra_context=extra_context)


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	list_display = (
		"idOrder", "date", "total_price", "customer_name", "customer_surname", "customer_phone", "delivery", "payment",
		"status")
	list_filter = ("status",)
	inlines = [
		OrderItemInline,
	]

	def idOrder(self, obj):
		return 'Заказ № %s' % str(obj.id)

	idOrder.short_description = "Номер заказа"

	def save_model(self, request, obj, form, change):
		obj.save()


class ProductAvailabilityAdmin(admin.ModelAdmin):
	list_display = ("product", "quantity", "size")
	list_filter = ("product",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(TableOfSize)
admin.site.register(Size)
admin.site.register(ProductAvailability, ProductAvailabilityAdmin)
admin.site.site_title = "HOODIYALKO"
admin.site.site_header = "HOODIYALKO"
