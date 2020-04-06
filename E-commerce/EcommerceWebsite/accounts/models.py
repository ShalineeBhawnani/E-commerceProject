from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserModel(AbstractBaseUser):
    phone_number = models.CharField(max_length=10,unique=True)