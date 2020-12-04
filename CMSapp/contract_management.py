import django
import os
from django.shortcuts import render
from CMSapp import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()


def right(request):
    if request.session.get('is_login', None):
        response={}
        response['function'] = 'right'
        response['functionname'] = '权限管理'
        response['rownum'] = 5
        response['colnum'] = 4
        query_result = models.right.objects.all()
        totalnum = query_result.count()
        print(totalnum)
        print("111111111111111111111111111111")
        print(models.user.objects.all()[0].username)
        print(query_result[0].username.username)
        if totalnum > 5:
            resultlist = query_result[:5]
        else:
            resultlist = query_result

        response['resultlist']=resultlist
        return render(request, 'CMSapp/baseTable.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')
