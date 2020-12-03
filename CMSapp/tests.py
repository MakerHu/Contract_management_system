from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")# project_name 项目名称
django.setup()

from CMSapp import models
# Create your tests here.

models.user.objects.get(username='jjj').delete()