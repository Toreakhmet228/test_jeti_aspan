from django.contrib import admin
from .models import  Product,Store,City,CustomUser

# Registfroer your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(Store)
class Store(admin.ModelAdmin):
    pass

@admin.register(City)
class City(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    pass