from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import NewUserManager

# Create your models here.
class NewUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    objects = NewUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    def __str__(self) -> str:
        return self.get_full_name()

    USERNAME_FIELD = 'email'
