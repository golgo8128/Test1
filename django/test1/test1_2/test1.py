

from django.contrib.auth.models import User
from appDummy1.models import *

testtbl = TestTable1(
    user1 = User.objects.get(username = "rsaito"),
)

