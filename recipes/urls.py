from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='recipes'),
    path('<recipes_id>', views.recipes_detail, name='recipes_detail'),
    # reccipes_detail
]