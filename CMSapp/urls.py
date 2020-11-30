from django.urls import path
from CMSapp import views
from CMSapp import contract_management

urlpatterns = [
    #主页
    path('index/',contract_management.index),
    #登陆
    path('login/', views.view_login),
    #注册
    path('register/', views.view_register),


    # ajax
    path('ajax_login/', views.ajax_login),
    path('ajax_register/', views.ajax_register),
    path('ajax_confirm_username/', views.ajax_confirm_username),
]
