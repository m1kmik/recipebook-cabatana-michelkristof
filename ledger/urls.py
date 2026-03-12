from django.urls import path
from . import views
from .views import recipe_detail, recipe_list

urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
]
