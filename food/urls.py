from django.urls import path

from . import views

urlpatterns = [
    path('', views.foodview, name='foodview'),
    path('<int:id>', views.single_food, name='single_food'),
    path('<int:id>/edit', views.single_food_edit, name='single_food_edit')
]