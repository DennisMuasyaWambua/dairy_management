from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('dairy_owner', 'Dairy owner'),
    ('farmer', 'Farmer')
)


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=8, unique=True)
    short_name = models.CharField(choices=ROLE_CHOICES, default="farmer", max_length=255)
    description = models.CharField(max_length=255)


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=255, default="email@email.com")
    phone = models.CharField(verbose_name='Phone number', max_length=20, unique=True, null=False)
    password = models.CharField(verbose_name="password", max_length=255)
    username = models.CharField(verbose_name='username', max_length=20, unique=True, null=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name", "password", "username"]

# create the other types of users for the application
# class Dairy(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='Dairy')
#     name = models.CharField(max_length=100, default="dairy")
#     id_number = models.IntegerField(verbose_name="Id number")
#     phone = models.CharField(verbose_name='Phone number', max_length=20, unique=True)
#     location = models.CharField(verbose_name="Location", max_length=100)
#     password = models.CharField(verbose_name="password", max_length=255, default="dairy")
#     username = None
#
#     USERNAME_FIELD = "phone"
#     REQUIRED_FIELDS = ["name", "phone", "password"]
#
#
# class Farmer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='Farmer')
#     name = models.CharField(max_length=100, default="farmer")
#     id_number = models.IntegerField(verbose_name="Id number",)
#     phone = models.CharField(verbose_name='Phone number', max_length=20, unique=True)
#     password = models.CharField(verbose_name="password", max_length=255, default="farmer")
#     location = models.CharField(verbose_name="Location", max_length=100)
#     dairy = models.ForeignKey(Dairy, on_delete=models.CASCADE, related_name='Dairy')
#     username = None
#
#     USERNAME_FIELD = "phone"
#     REQUIRED_FIELDS = ["name", "phone", "password"]
