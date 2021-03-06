import django
import os

from django.db.models import Q
from django.shortcuts import render
from CMSapp import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()

# 将授权信息表基本信息发送给前端
def base_right_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/searchright/'
    # 返回搜索框中的值
    if is_search == 'true':
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

# 进入权限管理界面
def right(request):
    if request.session.get('is_login', None):
        # 查询结果
        query_result = models.right.objects.all()

        return base_right_table(request, query_result)
    else:
        return render(request, 'CMSapp/timeout.html')

# 权限管理搜索功能
def search_right(request):
    if request.session.get('is_login', None):
        searchMsg = request.POST.get('searchMsg')
        if searchMsg:
            # 查询结果
            query_result = []
            query_result.extend(models.right.objects.filter(Q(username__username__icontains=searchMsg) | Q(rolename__rolename__icontains=searchMsg)))

        else:
            query_result = models.right.objects.all()
        return base_right_table(request, query_result, 'true')
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 新用户权限分配
def base_newuser_authorize_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_newuser_authorize/'
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['用户名', '角色名', '操作']

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'newuser_authorize'
    response['functionname'] = '新用户授权'

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


def newuser_authorize(request):
    if request.session.get('is_login', None):
        # 查询结果
        query_result = models.right.objects.filter(rolename='newuser')
        return base_newuser_authorize_table(request, query_result)
    else:
        return render(request, 'CMSapp/timeout.html')


def search_newuser_authorize(request):
    if request.session.get('is_login', None):
        searchMsg = request.POST.get('searchMsg')
        if searchMsg:
            # 查询结果
            query_result = []
            query_result.extend(
                models.right.objects.filter(username__username__icontains=searchMsg, rolename='newuser'))
        else:
            query_result = models.right.objects.filter(rolename='newuser')
        return base_newuser_authorize_table(request, query_result, 'true')
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 待定稿合同
def base_pending_contract_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_pending_contract/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '定稿人', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'pending_contract'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '待定稿合同'  ########################## 这里要根据情况修改

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


def pending_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_state.objects.filter(type=2)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_state.objects.filter(type=2,
                                                                conid__username=username)  ########################## 这里要根据情况修改
        return base_pending_contract_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_pending_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_state.objects.filter(conid__conname__icontains=searchMsg,
                                                         type=2))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg, type=2))
            else:
                query_result.extend(
                    models.contract_state.objects.filter(conid__conname__icontains=searchMsg, type=2,
                                                         conid__username=username))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg, type=2,
                                                         conid__username=username))
        else:
            if rolename == 'root':
                query_result = models.contract_state.objects.filter(type=2)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_state.objects.filter(type=2,
                                                                    conid__username=username)  ########################## 这里要根据情况修改
        return base_pending_contract_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# 已定稿合同

def base_finalized_contract_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_finalized_contract/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '定稿人', '定稿时间']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'finalized_contract'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '已定稿合同'  ########################## 这里要根据情况修改

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


def finalized_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_state.objects.filter(type=3)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_state.objects.filter(type=3,
                                                                conid__username=username)  ########################## 这里要根据情况修改
        return base_finalized_contract_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_finalized_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_state.objects.filter(conid__conname__icontains=searchMsg,
                                                         type=3))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg, type=3))
            else:
                query_result.extend(
                    models.contract_state.objects.filter(conid__conname__icontains=searchMsg, type=3,
                                                         conid__username=username))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg, type=3,
                                                         conid__username=username))
        else:
            if rolename == 'root':
                query_result = models.contract_state.objects.filter(type=3)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_state.objects.filter(type=3,
                                                                    conid__username=username)  ########################## 这里要根据情况修改
        return base_finalized_contract_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 流程查询
def base_process_query_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_process_query/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '起草人', '修改时间', '状态','操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'process_query'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '流程查询'  ########################## 这里要根据情况修改

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


def process_query(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_state.objects.all()  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_state.objects.filter(
                conid__username=username)  ########################## 这里要根据情况修改
        return base_process_query_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_process_query(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_state.objects.filter(
                        conid__conname__icontains=searchMsg))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg))
            else:
                query_result.extend(
                    models.contract_state.objects.filter(conid__conname__icontains=searchMsg,
                                                         conid__username=username))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_state.objects.filter(conid__username__username__icontains=searchMsg,
                                                         conid__username=username))
        else:
            if rolename == 'root':
                query_result = models.contract_state.objects.all()  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_state.objects.filter(
                    conid__username=username)  ########################## 这里要根据情况修改
        return base_process_query_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 待会签合同 起草完成
def base_countersigning_contract_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_countersigning_contract/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '会签员', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response[
        'function'] = 'countersigning_contract'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '待会签合同'  ########################## 这里要根据情况修改

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


def countersigning_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            # 起草完成，会签未完成
            query_result = models.contract_process.objects.filter(type=1, state=0, conid__contract_state__type=1)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_process.objects.filter(type=1, state=0,
                                                                  username=username, conid__contract_state__type=1)  ########################## 这里要根据情况修改
            print(query_result)
        return base_countersigning_contract_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_countersigning_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=1,
                                                           state=0, conid__contract_state__type=1))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=1, state=0, conid__contract_state__type=1))
            else:
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=1, state=0,
                                                           username=username, conid__contract_state__type=1))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=1, state=0,
                                                           username=username, conid__contract_state__type=1))
        else:
            if rolename == 'root':
                query_result = models.contract_process.objects.filter(type=1,
                                                                      state=0, conid__contract_state__type=1)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_process.objects.filter(type=1, state=0,
                                                                      username=username, conid__contract_state__type=1)  ########################## 这里要根据情况修改
        return base_countersigning_contract_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 已会签合同 待定稿
def base_countersigned_contract_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_countersigned_contract/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '会签员', '修改时间']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response[
        'function'] = 'countersigned_contract'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '已会签合同'  ########################## 这里要根据情况修改

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


def countersigned_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_process.objects.filter(type=1, state=1)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_process.objects.filter(type=1, state=1,
                                                                  username=username)  ########################## 这里要根据情况修改
        return base_countersigned_contract_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_countersigned_contract(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=1,
                                                           state=1))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=1, state=1))
            else:
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=1, state=1,
                                                           username=username))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=1, state=1,
                                                           username=username))
        else:
            if rolename == 'root':
                query_result = models.contract_process.objects.filter(type=1,
                                                                      state=1)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_process.objects.filter(type=1, state=1,
                                                                      username=username)  ########################## 这里要根据情况修改
        return base_countersigned_contract_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 待审批合同 审批未完成
def base_contract_approving_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_approving/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '审批员', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'contract_approving'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '待审批合同'  ########################## 这里要根据情况修改

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


def contract_approving(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        query_result=[]
        if rolename == 'root':
            # 查询结果
            # 审批未完成或审批被拒绝，起草完成
            query_result.extend(models.contract_process.objects.filter(type=2, state=0,conid__contract_state__type=3) ) ########################## 这里要根据情况修改
            query_result.extend(models.contract_process.objects.filter(type=2, state=2, conid__contract_state__type=3))
        else:
            query_result.extend(models.contract_process.objects.filter(type=2, state=0,
                                                                  username=username,conid__contract_state__type=3))  ########################## 这里要根据情况修改
            query_result.extend(models.contract_process.objects.filter(type=2, state=2,
                                                                       username=username,
                                                                       conid__contract_state__type=3))
        return base_contract_approving_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_approving(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                # 审批未完成
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2,
                                                           state=0,conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=0,conid__contract_state__type=3))
                # 审批被拒绝
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2,
                                                           state=2,
                                                           conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=2,
                                                           conid__contract_state__type=3))
            else:
                # 审批未完成
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2, state=0,
                                                           username=username,conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=0,
                                                           username=username,conid__contract_state__type=3))
                # 审批被拒绝
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2, state=2,
                                                           username=username,
                                                           conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=2,
                                                           username=username, conid__contract_state__type=3))
        else:
            if rolename == 'root':
                query_result.extend(models.contract_process.objects.filter(type=2,
                                                                      state=0,conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(models.contract_process.objects.filter(type=2,
                                                                           state=2, conid__contract_state__type=3))
            else:
                query_result.extend(models.contract_process.objects.filter(type=2, state=0,
                                                                      username=username,conid__contract_state__type=3))  ########################## 这里要根据情况修改
                query_result.extend(models.contract_process.objects.filter(type=2, state=2,
                                                                           username=username,
                                                                           conid__contract_state__type=3))
        return base_contract_approving_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 已审批合同
def base_contract_approved_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_approved/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '审批员', '起草时间']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'contract_approved'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '已审批合同'  ########################## 这里要根据情况修改

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


def contract_approved(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        query_result = []
        if rolename == 'root':
            # 查询结果
            query_result.extend(
                models.contract_process.objects.filter(type=2, state=1))  ########################## 这里要根据情况修改
            query_result.extend(models.contract_process.objects.filter(type=2, state=2))  # 审批已否决
        else:
            query_result.extend(models.contract_process.objects.filter(type=2, state=1,
                                                                       username=username))  ########################## 这里要根据情况修改
            query_result.extend(models.contract_process.objects.filter(type=2, state=2, username=username))
        return base_contract_approved_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_approved(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                # 审批已通过
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2,
                                                           state=1))
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=1))
                # 审批已否决
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2,
                                                           state=2))
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=2))
            else:
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2, state=1,
                                                           username=username))  #审批已通过
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=1,
                                                           username=username))  # 审批已通过
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=2, state=2,
                                                           username=username))  # 审批已否决
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=2, state=2,
                                                           username=username))  # 审批已否决
        else:
            if rolename == 'root':
                query_result.extend(models.contract_process.objects.filter(type=2, state=1))
                query_result.extend(models.contract_process.objects.filter(type=2, state=2))
            else:
                query_result.extend(models.contract_process.objects.filter(type=2, state=1, username=username))
                query_result.extend(models.contract_process.objects.filter(type=2, state=2, username=username))
        return base_contract_approved_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


# 待签订合同
def base_contract_signing_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_signing/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '签订人', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'contract_signing'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '待签订合同'  ########################## 这里要根据情况修改

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


def contract_signing(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_process.objects.filter(type=3, state=0,conid__contract_state__type=4)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_process.objects.filter(type=3, state=0,
                                                                  username=username,conid__contract_state__type=4)  ########################## 这里要根据情况修改
        return base_contract_signing_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_signing(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=3,
                                                           state=0,conid__contract_state__type=4))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=3, state=0,conid__contract_state__type=4))
            else:
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=3, state=0,
                                                           username=username,conid__contract_state__type=4))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=3, state=0,
                                                           username=username,conid__contract_state__type=4))
        else:
            if rolename == 'root':
                query_result = models.contract_process.objects.filter(type=3,
                                                                      state=0,conid__contract_state__type=4)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_process.objects.filter(type=3, state=0,
                                                                      username=username,conid__contract_state__type=4)  ########################## 这里要根据情况修改
        return base_contract_signing_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 已签订合同
def base_contract_signed_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_signed/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '签订人', '修改时间']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'contract_signed'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '已签订合同'  ########################## 这里要根据情况修改

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


def contract_signed(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_process.objects.filter(type=3, state=1)  ########################## 这里要根据情况修改
        else:
            query_result = models.contract_process.objects.filter(type=3, state=1,
                                                                  username=username)  ########################## 这里要根据情况修改
        return base_contract_signed_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_signed(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=3,
                                                           state=1))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=3, state=1))
            else:
                query_result.extend(
                    models.contract_process.objects.filter(conid__conname__icontains=searchMsg, type=3, state=1,
                                                           username=username))  ########################## 这里要根据情况修改
                query_result.extend(
                    models.contract_process.objects.filter(username__username__icontains=searchMsg, type=3, state=1,
                                                           username=username))
        else:
            if rolename == 'root':
                query_result = models.contract_process.objects.filter(type=3,
                                                                      state=1)  ########################## 这里要根据情况修改
            else:
                query_result = models.contract_process.objects.filter(type=3, state=1,
                                                                      username=username)  ########################## 这里要根据情况修改
        return base_contract_signed_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 已签订合同 重复
# def base_contract_signed_table(request, query_result, is_search='false'):
#     # 返回给界面的值
#     response = {}
#
#     response['searchURL'] = '/search_contract_signed/'     ########################## 这里要根据情况修改
#     # 返回搜索框中的值
#     if is_search == 'true':
#         # 搜索条件
#         searchMsg = request.POST.get('searchMsg')
#         response['searchMsg'] = searchMsg
#
#     # 获取选择的页数
#     pageNum = int(request.POST.get('pageNum'))
#
#     # 字段列表
#     fieldlist = ['合同编号', '合同名称', '起草时间']      ########################## 这里要根据情况修改
#
#     response['fieldlist'] = fieldlist
#
#     # 功能的中英文名
#     response['function'] = 'contract_signed'   ########################## 这里要根据情况修改        ******名字从base.html里找******
#     response['functionname'] = '已签订合同'      ########################## 这里要根据情况修改
#
#     # 翻页页码
#     if pageNum == 1:
#         pageslist = [str(pageNum), str(pageNum + 1), str(pageNum + 2), str(pageNum + 3), str(pageNum + 4)]
#     elif pageNum == 2:
#         pageslist = [str(pageNum - 1), str(pageNum), str(pageNum + 1), str(pageNum + 2), str(pageNum + 3)]
#     else:
#         pageslist = [str(pageNum - 2), str(pageNum - 1), str(pageNum), str(pageNum + 1), str(pageNum + 2)]
#
#     response['pageslist'] = pageslist
#
#     # 当前页码
#     response['current_page'] = str(pageNum)
#
#     # 返回结果列表，需要的五条记录
#     startindex = (5 * (pageNum - 1))
#     endindex = startindex + 5
#     resultlist = query_result[startindex:endindex]
#
#     response['resultlist'] = resultlist
#     return render(request, 'CMSapp/baseTable.html', response)
#
#
# def contract_signed(request):
#     if request.session.get('is_login', None):
#         username = request.session.get('username')
#         rolename = models.right.objects.filter(username=username)[0].rolename.rolename
#         if rolename == 'root':
#             # 查询结果
#             query_result = models.contract_state.objects.filter(type=5)     ########################## 这里要根据情况修改
#         else:
#             query_result = models.contract_state.objects.filter(type=5, conid__username=username)   ########################## 这里要根据情况修改
#         return base_contract_signed_table(request, query_result)       ########################## 这里要根据情况修改
#     else:
#         return render(request, 'CMSapp/timeout.html')
#
#
# def search_contract_signed(request):
#     if request.session.get('is_login', None):
#         username = request.session.get('username')
#         rolename = models.right.objects.filter(username=username)[0].rolename.rolename
#         searchMsg = request.POST.get('searchMsg')
#         query_result = []
#         if searchMsg:
#             # 查询结果
#             if rolename == 'root':
#                 query_result.extend(
#                     models.contract_state.objects.filter(conid__conname__icontains=searchMsg, type=5))  ########################## 这里要根据情况修改
#             else:
#                 query_result.extend(
#                     models.contract_state.objects.filter(conid__conname__icontains=searchMsg, type=5, conid__username=username))    ########################## 这里要根据情况修改
#         else:
#             if rolename == 'root':
#                 query_result = models.contract_state.objects.filter(type=5)  ########################## 这里要根据情况修改
#             else:
#                 query_result = models.contract_state.objects.filter(type=5, conid__username=username)  ########################## 这里要根据情况修改
#         return base_contract_signed_table(request, query_result, 'true')           ########################## 这里要根据情况修改
#     else:
#         return render(request, 'CMSapp/timeout.html')

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 待分配合同
def base_contract_distributing_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_distributing/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '起草人', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response[
        'function'] = 'contract_distributing'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '待分配合同'  ########################## 这里要根据情况修改

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


def contract_distributing(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果0
            query_result = models.contract_state.objects.exclude(Q(conid__conid__in=models.contract_process.objects.all().values('conid__conid')) | Q(type=6))  ########################## 这里要根据情况修改
        return base_contract_distributing_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_distributing(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                query_result = models.contract_state.objects.exclude(
                    conid__conid__in=models.contract_process.objects.all().values(
                        'conid__conid'))  ########################## 这里要根据情况修改
                query_result = query_result.filter(conid__conname__icontains=searchMsg)
        else:
            if rolename == 'root':
                query_result = models.contract_state.objects.exclude(
                    conid__conid__in=models.contract_process.objects.all().values(
                        'conid__conid'))  ########################## 这里要根据情况修改
        return base_contract_distributing_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 已分配合同
def base_contract_distributed_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_contract_distributed/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['合同编号', '合同名称', '起草人', '修改时间', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response[
        'function'] = 'contract_distributed'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '已分配合同'  ########################## 这里要根据情况修改

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


def contract_distributed(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        if rolename == 'root':
            # 查询结果
            query_result = models.contract_state.objects.filter(
                conid__conid__in=models.contract_process.objects.all().values(
                    'conid__conid'))  ########################## 这里要根据情况修改
        return base_contract_distributed_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_contract_distributed(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            if rolename == 'root':
                # query_result = models.contract_state.objects.filter(
                #     conid__conid__in=models.contract_process.objects.all().values(
                #         'conid__conid'))  ########################## 这里要根据情况修改
                # query_result = query_result.filter(conid__conname__icontains=searchMsg)
                query_result = models.contract_state.objects.filter(
                    conid__conid__in=models.contract_process.objects.filter(Q(conid__conname__icontains=searchMsg) | Q(conid__username__username__icontains=searchMsg)).values(
                        'conid__conid'))  ########################## 这里要根据情况修改
        else:
            if rolename == 'root':
                query_result = models.contract_state.objects.filter(
                    conid__conid__in=models.contract_process.objects.all().values(
                        'conid__conid'))  ########################## 这里要根据情况修改
        return base_contract_distributed_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 客户信息
def base_customer_info_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_customer_info/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['客户编号', '客户姓名', '客户电话', '操作']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'customer_info'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '客户信息'  ########################## 这里要根据情况修改

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


def customer_info(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        # 查询结果
        query_result = models.customer.objects.filter()  ########################## 这里要根据情况修改
        return base_customer_info_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_customer_info(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        rolename = models.right.objects.filter(username=username)[0].rolename.rolename
        searchMsg = request.POST.get('searchMsg')
        query_result = []
        if searchMsg:
            # 查询结果
            query_result = models.customer.objects.filter(
                cusname__icontains=searchMsg)  ########################## 这里要根据情况修改
        else:
            query_result = models.customer.objects.filter()  ########################## 这里要根据情况修改
        return base_customer_info_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# 日志信息
def base_view_log_table(request, query_result, is_search='false'):
    # 返回给界面的值
    response = {}

    response['searchURL'] = '/search_view_log/'  ########################## 这里要根据情况修改
    # 返回搜索框中的值
    if is_search == 'true':
        # 搜索条件
        searchMsg = request.POST.get('searchMsg')
        response['searchMsg'] = searchMsg

    # 获取选择的页数
    pageNum = int(request.POST.get('pageNum'))

    # 字段列表
    fieldlist = ['用户名', '操作对象', '内容', '操作时间']  ########################## 这里要根据情况修改

    response['fieldlist'] = fieldlist

    # 功能的中英文名
    response['function'] = 'view_log'  ########################## 这里要根据情况修改        ******名字从base.html里找******
    response['functionname'] = '日志信息'  ########################## 这里要根据情况修改

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


def view_log(request):
    if request.session.get('is_login', None):
        username = request.session.get('username')
        # 查询结果
        query_result = models.log.objects.all()  ########################## 这里要根据情况修改
        return base_view_log_table(request, query_result)  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')


def search_view_log(request):
    if request.session.get('is_login', None):
        searchMsg = request.POST.get('searchMsg')
        if searchMsg:
            # 查询结果
            query_result=models.log.objects.filter(Q(username__icontains=searchMsg) | Q(operateobject__icontains=searchMsg))
        else:
            query_result = models.log.objects.all()  ########################## 这里要根据情况修改
        return base_view_log_table(request, query_result, 'true')  ########################## 这里要根据情况修改
    else:
        return render(request, 'CMSapp/timeout.html')

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
