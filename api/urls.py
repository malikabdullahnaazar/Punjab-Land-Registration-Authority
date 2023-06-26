from django.urls import path
from . import views

urlpatterns = [
    path('/userApi', views.userApi),
]
