from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class TestTable1(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)

