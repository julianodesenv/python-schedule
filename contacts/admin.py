from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone', 'created_at', 'category', 'view')

    list_display_links = ('id', 'name', 'last_name')
    #list_filter = ('name', 'last_name')
    list_per_page = 10
    search_fields = ('name', 'last_name', 'phone')
    list_editable = ('phone', 'view')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
