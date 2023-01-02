from django.urls import path
from . import views

urlpatterns =[
    path('',views.yummy),
    path('register', views.register, name ='register')
]