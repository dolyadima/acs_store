from django.contrib import admin

from .models import Product, Category, Shop, Sale


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ("title", "category", "amount", "price", "shop", )
    list_filter = ("category", "shop", )


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("title", )


class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = ("address", )


class SaleAdmin(admin.ModelAdmin):
    model = Sale
    list_display = ("date_time", "product", "amount", "price", )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Sale, SaleAdmin)
