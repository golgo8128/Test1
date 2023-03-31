

from django.contrib.auth.models import User
from appTest1.models import *

testtbl = TestTable1(
    user1 = User.objects.get(username = "rsaito"),
    out1  = TestItem1.objects.create(str1 = "Test")
)

