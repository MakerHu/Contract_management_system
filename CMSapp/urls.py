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
    path('newuser_authorize/',contract_management.newuser_authorize),
    path('search_newuser_authorize/', contract_management.search_newuser_authorize),

    # ajax
    path('ajax_login/', views.ajax_login),
    path('ajax_register/', views.ajax_register),
    path('ajax_confirm_username/', views.ajax_confirm_username),
    path('ajax_distribution/', data_management.test),
]
