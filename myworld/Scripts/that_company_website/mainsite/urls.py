from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aboutus/', views.about, name='about'),
    path('mainsite/', views.mainsite, name='mainsite'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]