# File: views.py
# Author: Victoria Lin (vicki@bu.edu), 10/7/2024
# Description: gets all profile records from the database 
# and passes them to show_all_profiles.html

from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

class ShowAllProfilesView(ListView):
    """
    displays all user profiles stored in the database
    """
    model = Profile

    # The template displays the list of profiles
    template_name = 'mini_fb/show_all_profiles.html'

    # allows us to access the data in the template
    context_object_name = 'profiles'