from django.urls import path
from . import views
from .views import RecipeDetailView

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]

app_name = "recipes"  
