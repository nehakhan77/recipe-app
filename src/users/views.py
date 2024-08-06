from django.shortcuts import render
from django.views.generic import DetailView
from .models import User

class profile(DetailView):                      #class-based view
   model = User                                      #specify model
   template_name = 'users/user_profile.html'                 #specify template

