from django.contrib import admin
from .models import Products, Promotion, Categoty

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['collection']
    list_editable = ['price']
    list_per_page = 20
    # list_select_related = ['collection']
    search_fields = ['title']
    list_display = ['id', 'title',  'price', 'description', 'inventory']
    
@admin.register(Categoty)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Promotion)
class PromtotionAdmin(admin.ModelAdmin):
    list_display = ['id', 'description',  'discount']