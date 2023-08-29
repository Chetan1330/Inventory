from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import Stock, Class1, Category, Subcategory, Manufacturer, Model, Config, ConfigName


admin.site.site_header = 'Inventory_Next'

@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ('name', 'SSN', 'Class', 'Category', 'Manufacturer', 'Model', 'Reservedby', 'Reserved_at', 'Configname', 'Type', 'Count')

# admin.site.register(Stock)

admin.site.register(Class1)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Config)
admin.site.register(ConfigName)
