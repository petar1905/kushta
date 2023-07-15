from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.single, name='single'),
    path('<int:id>/edit', views.single_edit, name='single_edit')
]