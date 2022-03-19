from django.db.models.functions import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from django.shortcuts import render

class Todo(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)
        if end_date:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        Task.objects.create(user_id=user_id, task_name=name, end_date=end_date)

        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(dict(task_name=task.task_name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context = dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)

    def get(self, request):
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(dict(task_name=task.task_name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context=dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)



class TaskCreate(APIView):
    def post(self, request):
        user_id = request.data.get("user_id","")
        task_name = request.data.get("task_name","")
        end_date = request.data.get("end_date",None)

        if end_date:
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        task = Task.objects.create(user_id=user_id, task_name=task_name, end_date=end_date)

        data = dict(msg="Todo 생성완료", task_name=task.task_name,\
                    start_date = task.start_date.strftime("%Y-%m-%d"),\
                    end_date = task.end_date)


        return Response(data = data)

class TaskSelect(APIView):
    def post(self, request):
        user_id = request.data.get("user_id","")
        tasks = Task.objects.filter(user_id=user_id)
        task_list = []
        for task in tasks:
            task_list.append(dict(task_name = task.task_name, start_date = task.start_date,\
                                  end_date = task.end_date, state = task.state))
        return Response(dict(tasks = task_list))