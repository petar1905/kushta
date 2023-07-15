from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('login/error', views.login_error, name='login_error')
]