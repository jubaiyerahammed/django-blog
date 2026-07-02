from django.urls import path
from .import views
urlpatterns = [
    path('', views.deshboard, name='deshboard'),
    path('categories/', views.categories, name='categories' ),
    path('categories/add/', views.add_category, name='add_category'),
]