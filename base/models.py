from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone_num = models.CharField(max_length=15, null=True)
