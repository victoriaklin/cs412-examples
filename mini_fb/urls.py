# File: urls.py
# Author: Victoria Lin (vicki@bu.edu), 10/7/2024
# Description: Maps URLs to views

from django.urls import path
from .views import ShowAllProfilesView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
]