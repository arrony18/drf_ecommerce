from django.contrib import admin
from .models import Product,ProductLine,Category,Brand
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductLine)
admin.site.register(Category)
admin.site.register(Brand)