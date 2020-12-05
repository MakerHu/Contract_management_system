import django
import os
from django.shortcuts import render
from CMSapp import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()


def base_right_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/searchright/'
    # 返回搜索框中的值
    if is_search=='true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['用户名', '角色名', '操作']

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'right'
    response['functionname'] = '权限管理'

    # 翻页页码
    if pageNum == 1:
        pageslist = [str(pageNum), str(pageNum + 1), str(pageNum + 2), str(pageNum + 3), str(pageNum + 4)]
    elif pageNum == 2:
        pageslist = [str(pageNum - 1), str(pageNum), str(pageNum + 1), str(pageNum + 2), str(pageNum + 3)]
    else:
        pageslist = [str(pageNum - 2), str(pageNum - 1), str(pageNum), str(pageNum + 1), str(pageNum + 2)]

    response['pageslist'] = pageslist

    # 当前页码
    response['current_page'] = str(pageNum)

    # 返回结果列表，需要的五条记录
    startindex = (5 * (pageNum - 1))
    endindex = startindex + 5
    resultlist = query_result[startindex:endindex]

    response['resultlist'] = resultlist
    return render(request, 'CMSapp/baseTable.html', response)


def right(request):
    if request.session.get('is_login', None):
        # 查询结果
        query_result = models.right.objects.all()
        return base_right_table(request, query_result)
    else:
        return render(request, 'CMSapp/timeout.html')


def search_right(request):
    if request.session.get('is_login', None):
        searchMsg = request.POST.get('searchMsg')
        if searchMsg:
            # 查询结果
            query_result =[]
            query_result.extend(models.right.objects.filter(username__username__icontains=searchMsg))
            query_result.extend(models.right.objects.filter(rolename__rolename__icontains=searchMsg))
        else:
            query_result = models.right.objects.all()
        return base_right_table(request, query_result, 'true')
    else:
        return render(request, 'CMSapp/timeout.html')
