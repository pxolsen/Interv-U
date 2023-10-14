from collections.abc import Collection
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .validators import validate_name
# from .managers import CustomUserManager

class Client(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(validators=[validate_name])
    last_name = models.CharField(validators=[validate_name])
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile_pics/")

    # groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='custom_user_permissions')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # def __str__(self):
    #     return self.email
    
    # def full_clean(self, exclude=None, validate_unique=True):
    #     # Exclude 'username' field from validation
    #     if exclude is None:
    #         exclude = []
    #     exclude.append('username')
    #     super().full_clean(exclude=exclude, validate_unique=validate_unique)

    # objects = CustomUserManager()   