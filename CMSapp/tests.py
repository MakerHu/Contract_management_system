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
models.customer.objects.get_or_create(cusid=1, cusname='客户1', address='福建', tel='13156')
cusEntity = models.customer.objects.filter(cusid=1)[0]
userEntity = models.user.objects.filter(username='ydz')[0]
models.contract.objects.get_or_create(conname='合同1', username=userEntity, cusid=cusEntity, begintime='2020-05-03',
                                      endtime='2020-10-12')
contractEntity = models.contract.objects.filter(conid=2)[0]
models.contract_state.objects.get_or_create(type=1, conid=contractEntity)


models.customer.objects.get_or_create(cusid=3, cusname='客户3', address='上海', tel='13156')
cusEntity = models.customer.objects.filter(cusid=3)[0]
userEntity = models.user.objects.filter(username='hhh')[0]
models.contract.objects.get_or_create(conid='3', conname='合同3', username=userEntity, cusid=cusEntity,content='lfksdj', begintime='2020-05-03',
                                      endtime='2020-10-12')
contractEntity = models.contract.objects.filter(conid=3)[0]
models.contract_state.objects.get_or_create(type=1, conid=contractEntity)
