from django.urls import path
from .views import RecipeListView, RecipeDetailView
from .views import home

app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path('recipes/', RecipeListView.as_view(), name='list'),
   path('recipes/<int:pk>', RecipeDetailView.as_view(), name='detail'),
]