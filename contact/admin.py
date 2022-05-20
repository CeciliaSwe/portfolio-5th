from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message',)

admin.site.register(Contact, ContactAdmin)
