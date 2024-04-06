from atexit import register
from django.contrib import admin
from .models import *
 
 

class AdminCategory(admin.ModelAdmin):
  list_display = ['name']
class AdminProduct(admin.ModelAdmin):
  list_display = ['name']
class AdminCart(admin.ModelAdmin):
  list_display = ['user','product']
class AdminFavourite(admin.ModelAdmin):
  list_display = ['user','product']



admin.site.register(Category,AdminCategory) 
admin.site.register(Product,AdminProduct)
admin.site.register(Cart,AdminCart)
admin.site.register(Favourite,AdminFavourite)