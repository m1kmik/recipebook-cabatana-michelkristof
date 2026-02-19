from django.urls import path
from .views import recipe_list

urlpatterns = [
path('list', recipe_list, name="recipe-list"),
]

# This might be needed, depending on your Django version
app_name = "recipe"