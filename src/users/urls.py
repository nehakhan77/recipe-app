from django.urls import path
from .views import profile

app_name = 'users'

urlpatterns = [
  path('profile/<int:pk>', profile.as_view(), name="profile")
]