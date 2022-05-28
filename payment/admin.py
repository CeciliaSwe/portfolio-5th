from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       )

    fields = ('order_number', 'user_profile',
              'date', 'first_name', 'last_name',
              'email', 'phone_number', 'country',
              'zipcode', 'city', 'street_address1',
              'street_address2', 'county')

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
