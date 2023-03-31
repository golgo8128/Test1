


from django.contrib.auth.models import User

User.objects.all().delete()
User.objects.create_superuser('rsaito',
                              'golgo8128@yahoo.co.jp',
                              'easypass')

