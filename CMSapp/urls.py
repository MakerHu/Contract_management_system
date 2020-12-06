from django.urls import path
from CMSapp import views
from CMSapp import contract_management
from CMSapp import data_management

urlpatterns = [
    # 主页
    path('index/', views.index),

    # 首页
    path('home/', views.home),

    # 登录
    path('login/', views.view_login),
    # 登出
    path('logout/', views.logout),
    # 注册
    path('register/', views.view_register),
    # 起草合同
    path('draftcontract/', views.view_draft),

    # 权限管理
    path('right/', contract_management.right),

    # 查询权限表
    path('searchright/', contract_management.search_right),

    # 新用户权限分配
    path('newuser_authorize/', contract_management.newuser_authorize),
    path('search_newuser_authorize/', contract_management.search_newuser_authorize),

    # 待定稿合同
    path('pending_contract/', contract_management.pending_contract),
    path('search_pending_contract/', contract_management.search_pending_contract),

    # 已定稿合同
    path('finalized_contract/', contract_management.finalized_contract),
    path('search_finalized_contract/', contract_management.search_finalized_contract),

    # 流程查询
    path('process_query/', contract_management.process_query),
    path('search_process_query/', contract_management.search_process_query),

    # 待会签合同
    path('countersigning_contract/', contract_management.countersigning_contract),
    path('search_countersigning_contract/', contract_management.search_countersigning_contract),

    # 已会签合同
    path('countersigned_contract/', contract_management.countersigned_contract),
    path('search_countersigned_contract/', contract_management.search_countersigned_contract),

    #待审批合同
    path('contract_approving/' ,contract_management.contract_approving),
    path('search_contract_approving/', contract_management.search_contract_approving),

    #已审批合同
    path('contract_approved/', contract_management.contract_approved),
    path('search_contract_approved/', contract_management.search_contract_approved),

    #待签订合同
    path('contract_signing/', contract_management.contract_signing),
    path('search_contract_signing/', contract_management.search_contract_signing),

    #已签订合同
    path('contract_signed/', contract_management.contract_signed),
    path('search_contract_signed/', contract_management.search_contract_signed),

    # ajax
    path('ajax_login/', views.ajax_login),
    path('ajax_register/', views.ajax_register),
    path('ajax_confirm_username/', views.ajax_confirm_username),
    path('ajax_distribution/', data_management.test),

]
