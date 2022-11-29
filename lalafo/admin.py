from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Location)
admin.site.register(Category)
