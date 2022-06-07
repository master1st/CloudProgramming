from django.contrib import admin
from product.models import Product, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


admin.site.register(Product, ProductAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)