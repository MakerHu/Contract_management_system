import os,django
from django.forms import forms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")# project_name 项目名称
django.setup()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()