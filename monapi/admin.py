from django.contrib import admin

from .models import Car, Brand, CustomerService

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(CustomerService)
