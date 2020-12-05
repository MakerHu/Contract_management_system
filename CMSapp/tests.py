from django.test import TestCase
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()

from CMSapp import models

# Create your tests here.

# totalnum = query_result.count()
# if totalnum > 5:
#     resultlist = query_result[:5]
# else:
#     resultlist = query_result

# models.user.objects.get(username='hhh').delete()
# models.user.objects.all().delete()
# print(models.user.objects.all()[0].username)
print(models.user.objects.all())
