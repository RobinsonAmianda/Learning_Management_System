from django.urls import path
from . import views

urlpatterns = [
    path('login_view', views.login_view, name='login'),
    path('users', views.user_list, name='user_list'),
]