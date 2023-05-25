from django.contrib import admin
from .models import Stock, Class1, Category, Subcategory, Manufacturer, Model

admin.site.register(Stock)

admin.site.register(Class1)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Manufacturer)
admin.site.register(Model)