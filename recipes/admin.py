from django.contrib import admin

# Register your models here.
from . models import Recipes, Category, Comment

admin.site.register(Comment)
admin.site.register(Recipes)
admin.site.register(Category)
