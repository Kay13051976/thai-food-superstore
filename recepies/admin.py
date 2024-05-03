from django.contrib import admin

# Register your models here.
from . models import Recepies, Category, Comment

admin.site.register(Comment)
admin.site.register(Recepies)
admin.site.register(Category)
