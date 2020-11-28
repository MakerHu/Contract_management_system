from django.conf.urls import url
from CMSapp import views

urlpatterns = [
    url(r'^login/',views.view_login)

]
