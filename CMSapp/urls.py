from django.urls import path
from CMSapp import views
from CMSapp import contract_management

urlpatterns = [
    path('login/', views.view_login),
    path('register/', views.view_register),
    path('ajax_login/', views.ajax_login),
    path('index/',contract_management.index)
]
