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

conidentity = models.contract.objects.get(conid=1)
models.contract_state.objects.create(type=2,conid=conidentity).save()
models.customer.objects.create(cusname='客户1', address='福建',tel='13156').save()
models.contract.objects.create(conname='合同1',cusid=2,begintime='2020-05-03',endtime='2020-10-12')