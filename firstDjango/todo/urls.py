from django.urls import re_path as url
from .views import TaskCreate, TaskSelect

urlpatterns = [
    url('create',TaskCreate.as_view(),name= 'create'),
    url('select',TaskSelect.as_view(),name= 'select')
]