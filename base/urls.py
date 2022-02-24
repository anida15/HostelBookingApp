from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('hostels/', views.hostels, name = 'hostels'),
    path('users/', views.users, name = 'users'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
 ]