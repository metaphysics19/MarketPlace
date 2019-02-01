from django.contrib import admin
from .models import Comments
from .models import Category
from .models import Products


admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Products)
