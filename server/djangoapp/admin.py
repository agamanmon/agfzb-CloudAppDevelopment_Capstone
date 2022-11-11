from django.contrib import admin
from .models import *


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model=CarModel
    extra=2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display=['car_make']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines=[CarModelInline]


# Register models here
admin.site.register(CarModel,CarModelAdmin)
admin.site.register(CarMake,CarMakeAdmin)