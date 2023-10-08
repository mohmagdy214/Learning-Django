from django.contrib import admin
from .models import Product, Test

class ProductAdmin(admin.ModelAdmin):
    list_display =  ['name', 'price', 'active', 'category']
    list_display_links =  ['name']
    list_editable =  ['category', 'price', 'active']
    search_fields = ['name']
    list_filter = ['category']



# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Test)
admin.site.site_header = 'Megzz'
admin.site.site_title = 'Megzz'
