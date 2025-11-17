from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor','Doctor'),
        ('patient','Patient'),
        ('admin','Admin')
    )
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=15,choices=ROLE_CHOICES,default='patient')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.get_full_name()}"