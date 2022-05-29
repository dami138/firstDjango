from django.db import models
from django.utils import timezone


class Task(models.Model):
    user_id = models.CharField(max_length=20, null=False, default=False)
    task_name = models.CharField(max_length=20,verbose_name="작업이름",null=False, default='')#
    start_date = models.DateField(verbose_name="시작일",null=True, default=timezone.now)
    end_date = models.DateField(verbose_name="마감일",null=True)
    finished_date = models.DateField(verbose_name="완료일",null=True)
    state = models.IntegerField(verbose_name="상태",null=False, default=0)#

    class Meta:
        db_table = 'task'
        verbose_name = "Todo 테이블"