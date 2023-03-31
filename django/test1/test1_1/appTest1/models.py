from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User

class TestItem1(models.Model):
    str1 = models.CharField(max_length = 30)

class TestTable1(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    out1 = models.ForeignKey(TestItem1, on_delete=models.CASCADE)

