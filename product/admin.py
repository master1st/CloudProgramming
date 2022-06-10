from django.contrib import admin
from product.models import Product, Tag, Comment, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','pk')


admin.site.register(Product, ProductAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)
