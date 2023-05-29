from django.contrib import admin

# Register your models here.

from .models import Stock, Class1, Category, Subcategory, Manufacturer, Model, Config, ConfigName


admin.site.site_header = 'Inventory_Next'

admin.site.register(Stock)

admin.site.register(Class1)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Config)
admin.site.register(ConfigName)
