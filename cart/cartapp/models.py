from __future__ import unicode_literals

from django.db import models


class RegisterUsers(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        db_table = "registered_users"
# Create your models here.
