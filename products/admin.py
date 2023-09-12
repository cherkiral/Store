from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
