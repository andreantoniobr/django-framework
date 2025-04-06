from django.contrib import admin
from . import models
from .models import Product
from .models import Income
from .models import Expense

admin.site.register(models.Category)
#admin.site.register(models.Product)
admin.site.register(models.Client)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display = ('name', 'price', 'available', 'category', 'created_at')
 search_fields = ('name', 'category')
 list_filter = ('available', 'category')
 ordering = ('-created_at',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
 list_display = ('name', 'value', 'created_at')
 ordering = ('-created_at',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
 list_display = ('name', 'value', 'created_at')
 ordering = ('-created_at',)