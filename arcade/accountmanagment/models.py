# Imports
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password = None):
        if not email:
            raise ValueError("Users must have an email address!")
        if not username:
            raise ValueError("Users must have a username!")
        if not first_name:
            raise ValueError("Users must set their first name!")
        if not last_name:
            raise ValueError("Users must set their last name!")
        if not phone:
            raise ValueError("Users must set their phone number!")
        if not password:
            raise ValueError("Users must set a password!")
        
        user = self.model(
            email           = self.normalize_email(email),
            username        = username,
            first_name      = first_name,
            last_name       = last_name,
            phone           = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone, password):
        user = self.create_user(
            email           = self.normalize_email(email),
            password        = password,
            username        = username,
            first_name      = first_name,
            last_name       = last_name,
            phone           = phone,
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using = self._db)
        return user



# Custom user model
class User(AbstractUser):
    #Username is a defualt model so we don't have to write that here. 
    email           = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
    username        = models.CharField(max_length = 30, unique = True)
    first_name      = models.CharField(verbose_name = "first name", max_length = 30)
    last_name       = models.CharField(verbose_name = "last name", max_length = 30)
    phone           = models.CharField(null = True, max_length= 13)
    date_joined     = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login      = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = True)
    is_staff        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)

    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone",]

    #USERNAME_FIELD = "username"
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    objects = MyAccountManager()

    def __str__(self):
        return self.last_name + " " + self.first_name

    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True