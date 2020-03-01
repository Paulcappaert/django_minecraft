from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    mc_username = models.CharField(max_length=100)
    is_confirmed = models.BooleanField(default=False)
