from django.contrib import admin

# Register your models here.
from .models import TestTable1, TestItem1

admin.site.register(TestTable1)
admin.site.register(TestItem1)
