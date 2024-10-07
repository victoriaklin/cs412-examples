# File: models.py
# Author: Victoria Lin (vicki@bu.edu), 10/7/2024
# Description: creates and manages the database schema for the app

from django.db import models

class Profile(models.Model):
    """
    stores user profile information
    """
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
