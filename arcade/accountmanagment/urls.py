from os import name
from django.urls import path, include
from django.urls.resolvers import URLPattern
from accountmanagment import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('registeruser/', views.registerUser, name='registeruser'),
    path('checkserver/', views.index, name = 'checkserver'),
]