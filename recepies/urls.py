from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recepies, name='recepies'),
    path('<recepies_id>', views.recepies_detail, name='recepies_detail'),
    # recipe_detail
]