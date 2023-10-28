from django.contrib import admin
from .models import Car, Dealer, Customer, Sale

class CarAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'price')

class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','phone_number')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone_number')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'dealer', 'customer', 'sale_date')

admin.site.register(Car, CarAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)

