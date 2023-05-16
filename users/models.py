from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    country = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(upload_to='users/profile', blank=True)
    def __str__(self):
        return self.username