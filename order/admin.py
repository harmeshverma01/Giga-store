from django.contrib import admin
from .models import Order, OrderDetails

# Register your models here.

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'user', 'status']
    list_filter = ['status']
    search_fields = ['id']
    inlines = [OrderDetailsInline]

admin.site.register(Order,OrderAdmin)


    
    
