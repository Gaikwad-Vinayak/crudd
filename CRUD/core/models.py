from django.db import models
from django.contrib.auth.models import User
from datetime import timezone

# Create your models here.

class librarymanagement_module(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    formats = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    created_data_date = models.DateField(auto_now=True)
