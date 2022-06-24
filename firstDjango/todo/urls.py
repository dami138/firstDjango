from django.urls import re_path as url
from .views import TaskCreate, TaskSelect, TaskToggle, TaskDelete,Test

urlpatterns = [
    url('create',TaskCreate.as_view(),name= 'create'),
    url('select',TaskSelect.as_view(),name= 'select'),
    url('toggle',TaskToggle.as_view(),name= 'toggle'),
    url('delete',TaskDelete.as_view(),name= 'delete'),
    url('test',Test.as_view(),name= 'test')
]