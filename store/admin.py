from django.contrib import admin
from .models.product import Product
from .models.categories import Categories
from .models.customer import Customer
from .models.orders import Order

# Register your models here.

#class for showing data in adminpanel as table
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategories(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Product,AdminProduct)
admin.site.register(Categories,AdminCategories)
admin.site.register(Customer)
admin.site.register(Order)