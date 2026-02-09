from django.urls import path
from .views import recipe_1
from .views import recipe_2

urlpatterns = [
path('1', recipe_1, name="recipe-1"),
path('2', recipe_2, name="recipe-2"),
]

# This might be needed, depending on your Django version
app_name = "recipe"