from django.contrib import admin
from django.utils.html import format_html
from .novaposhta_api import invoice
from .models import Category, Product, ProductImage, Order, OrderItem, Size, ProductAvailability, TableOfSize, Localization
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib.admin.templatetags.admin_modify import register, submit_row as original_submit_row
from django import forms
from django.contrib import messages
from django.utils.translation import ngettext


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
    list_display = ('title', 'title_locale', 'get_price', 'category', 'get_image', 'admin_description', 'hidden', 'availability_info')
    list_filter = ['category']
    list_editable = ['hidden']
    inlines = [
        ProductImageInline,
        ProductAvailabilityInline
    ]
    autocomplete_fields = ['title_locale', 'description_locale']

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
        "id_order", "status_color", "format_datetime",
        "total_price_fix", "customer", "customer_phone", "delivery", "payment", "preorder")
    list_filter = ("status", "preorder",)
    exclude = ('total_price', "preorder")
    date_hierarchy = 'date'
    inlines = [
        OrderItemInline,
    ]
    actions = ['make_published']

    class Media:
        css = {
            "all": ("admin/css/my_style.css",)
        }
        js = ("admin/js/my_code.js",)

    def make_published(self, request, queryset):
        for i in range(0, len(queryset)):
            order_id = queryset[i].pk
            invoice(order_id)
        updated = queryset.update(status='3')
        self.message_user(request, ngettext(
            '%d накладная успешно создана.',
            '%d накладные успешно созданы.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "Создать накладную"

    def get_fields(self, request, obj):
        fields = list(super(OrderAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj:  # obj will be None on the add page, and something on change pages
            # exclude_set.add('post_office_ref')
            exclude_set.add('city_ref')
        return [f for f in fields if f not in exclude_set]

    def status_color(self, obj):
        status_text = None
        status_color = None
        text_color = "black"
        i = 0
        for el in Order.STATUS_CHOICE:
            if el[0] == obj.status:
                status_text = el[1]
                status_color = Order.STATUS_COLORS[i][1]
                break
            i += 1

        if obj.status in (Order.STATUS_CHOICE[0][0], Order.STATUS_CHOICE[2][0], Order.STATUS_CHOICE[3][0]):
            text_color = "white"

        return format_html(f'<div style="width:7rem; background-color: {status_color}; display: flex; '
                           f'justify-content: center; align-items: center; color: {text_color}">{status_text}</div>')

    status_color.allow_tags = True
    status_color.short_description = "Статус"

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(OrderAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'post_office':
            formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
        if db_field.name == 'address':
            formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
        return formfield

    def id_order(self, obj):
        return '%s' % str(obj.id)

    id_order.short_description = "№"

    def format_datetime(self, obj):
        new = str(obj.date.strftime('%b'))
        return '%s.%s, %s' % (str(obj.date.day), new, str(obj.date.strftime('%H:%M')))

    format_datetime.short_description = "Дата"

    def total_price_fix(self, obj):
        return str(obj.total_price_calc()).split('.')[0]

    total_price_fix.short_description = "Сумма"

    def customer(self, obj):
        return '%s %s' % (obj.customer_surname, obj.customer_name)

    customer.short_description = "Заказчик"

    def save_model(self, request, obj, form, change):
        obj.save()


class ProductAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "size", "preorder")
    list_editable = ['preorder']
    list_filter = ("product",)


class LocalizationAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "value_ua", "value_en")
    list_filter = ("key",)
    ordering = ("key",)
    search_fields = ("key",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "pk",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Localization, LocalizationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TableOfSize)
admin.site.register(Size)
admin.site.register(ProductAvailability, ProductAvailabilityAdmin)
admin.site.site_title = "HOODIYALKO"
admin.site.site_header = "HOODIYALKO"
