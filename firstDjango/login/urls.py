from django.urls import re_path as url
from .views import RegistUser, AppLogin

urlpatterns = [
    url('regist_user', RegistUser.as_view(), name= 'regist_user'),
    url('app_login', AppLogin.as_view(), name= 'app_login')
]

