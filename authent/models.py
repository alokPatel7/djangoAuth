from django.db import models

# Create your models here.


class UserDetails(models.Model):

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    userType = models.CharField(max_length=100, default="user")

    class Meta:
        db_table = "UserDetail"
