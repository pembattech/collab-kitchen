from django.urls import path

from .views import RecipeListAPIView, RecipeCreateAPIView, RecipeRetrieveAPIView

urlpatterns = [
    path('', RecipeListAPIView.as_view(), name = "recipe_list" ),
    path('create', RecipeCreateAPIView.as_view(), name = "recipe_create"),
    path('<int:pk>', RecipeRetrieveAPIView.as_view(), name = "recipe_retrieve"),
]
path