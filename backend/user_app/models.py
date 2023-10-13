from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    profile_pc = models.ImageField(upload_to="profile-pictures", null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name, last_name]
