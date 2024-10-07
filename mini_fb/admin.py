# File: admin.py
# Author: Victoria Lin (vicki@bu.edu), 10/7/2024
# Description: Profile model is registered here so that 
# admin users can add, edit, and delete profiles

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)