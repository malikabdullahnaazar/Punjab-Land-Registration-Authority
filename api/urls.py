from django.urls import path
from .views import userApi
from .views import loginApi
from rest_framework.authtoken import views

urlpatterns = [
    path('userApi/', userApi),
    path('loginApi/', loginApi),
    path('api-token-auth/', views.obtain_auth_token)
]
