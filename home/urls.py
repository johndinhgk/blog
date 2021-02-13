from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/contact/',views.contact,name='contact'),
    path('home/register/',views.register,name='register')
]

