from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager
from django.db import models
import uuid
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name =  models.CharField(max_length=50)
    email =  models.EmailField(unique=True)
    date = models.DateTimeField(auto_now=True, null=True)
    age = models.PositiveIntegerField(null=True)
    phone_number = PhoneNumberField()
    country_code = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    address = models.CharField(max_length=250, null=True)
    objects = UserManager()
    
    
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name', 'password']
    

    def __str__(self) -> str:
        return self.name