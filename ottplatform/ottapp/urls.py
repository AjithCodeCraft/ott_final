from django.contrib import admin
from django.urls import path, include

from .views import login_view, register

urlpatterns = [
    path('login/',login_view,name='login'),
    path('',register,name='register')

]