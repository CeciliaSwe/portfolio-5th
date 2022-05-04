from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total',
                       )


    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
