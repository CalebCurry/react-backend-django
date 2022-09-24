from django.contrib import admin
from customers.models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)