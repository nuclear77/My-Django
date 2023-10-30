from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('user/<int:user_id>', views.user_detail, name='user_detail'),
    path('event/registration/', views.event_registration, name='event_registration'),
]