from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='about-club'),
    path('logo/', views.logo, name='negr'),
]
