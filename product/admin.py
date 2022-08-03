from django.contrib import admin

from product.models import Product, ProductReal, ProductLikeUser, Category


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductReal)
admin.site.register(ProductLikeUser)