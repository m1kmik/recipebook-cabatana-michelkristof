from django.urls import path
from . import views
from .views import RecipeDetailView

urlpatterns = [
    path('list', views.recipe_list, name='recipe-list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe-detail'),

]

# This might be needed, depending on your Django version
app_name = "recipes"