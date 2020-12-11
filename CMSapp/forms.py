import os,django

from django import forms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")# project_name 项目名称
django.setup()

class UploadFileForm(forms.Form):
    filename = forms.CharField(max_length=100)
    filetype = forms.CharField(max_length=20)
    file = forms.FileField()