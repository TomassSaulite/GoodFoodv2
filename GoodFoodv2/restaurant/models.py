# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class customRest(AbstractUser):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     email = models.CharField(max_length=50, blank=True, null=True,unique=True)
#     country = models.CharField(max_length=3,blank=True, null=True)
#     city = models.CharField(max_length=3,blank=True, null=True)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name", "country", "city"]