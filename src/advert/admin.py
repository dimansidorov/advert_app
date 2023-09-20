from django.contrib import admin 
from .models import Category, City, Advert 


class CategoryAdmin(admin.ModelAdmin): 
    pass 


class CityAdmin(admin.ModelAdmin): 
    pass 


class AdvertAdmin(admin.ModelAdmin): 
    pass 


admin.site.register(Category, CategoryAdmin) 
admin.site.register(City, CityAdmin) 
admin.site.register(Advert, AdvertAdmin)
