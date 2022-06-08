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

#실습 3


class TaskSelect(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', None)
        page_number = request.data.get('page_number',None)
        print(user_id,page_number)

        if user_id and not "":
            tasks = Task.objects.filter(user_id = user_id)
        else:
            tasks = Task.objects.all()

        is_last_page = True

        if page_number is not None and page_number >= 0:
            if tasks.count() <= 10:
                pass
            elif tasks.count() <= (1+page_number) * 10:
                tasks = tasks[page_number * 10:]
            else:
                is_last_page = False
                tasks = tasks[page_number*10:(1+page_number)+10]
        else:
            pass


        task_list= []
        for task in tasks:
            task_list.append(dict(id=task.id,
                              name=task.task_name,
                              user_id = user_id,
                              state=task.state))

        return Response(status=200, data=dict(tasks=task_list, isLastPage=is_last_page))


class TaskCreate(APIView):
    def post(self, request):
        user_id = request.data.get("user_id",None)
        todo_id = request.data.get("todo_id",None)
        todo_name = request.data.get("name","")

        if todo_id:
            task = Task.objects.create(id = todo_id, user_id = user_id, task_name= todo_name)
        else:
            task = Task.objects.create(user_id = user_id, task_name = todo_name)


        return Response(data = dict(task.id))

#실습 2
#
# class TaskSelect(APIView):
#     def post(self, request):
#         tasks = Task.objects.all()
#         task_list = []
#
#         for task in tasks:
#             task_list.append(dict(id=task.id,
#                                name=task.task_name,
#                                state=task.state))
#
#         return Response(status=200, data=dict(tasks= task_list))

# class TaskCreate(APIView):
#     def post(self, request):
#         user_id = request.data.get("user_id",None)
#         todo_id = request.data.get("todo_id",None)
#         todo_name = request.data.get("name","")
#
#         Task.objects.create(id = todo_id, user_id = user_id, task_name= todo_name)
#
#         return Response()

class TaskToggle(APIView):
    def post(self, request):
        todo_id = request.data.get("todo_id")
        task = Task.objects.get(id=todo_id)

        if task:
            print(task.state)
            task.state = 0 if task.state is 1 else 1
            task.save()
        return Response()

class TaskDelete(APIView):
    def post(self, request):
        todo_id = request.data.get("todo_id")
        task = Task.objects.get(id=todo_id)
        if task:
            task.delete()

        return Response()

#실습 1


# class TaskCreate(APIView):
#     def post(self, request):
#         user_id = request.data.get("user_id","")
#         task_name = request.data.get("task_name","")
#         end_date = request.data.get("end_date",None)
#
#         if end_date:
#             end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
#         task = Task.objects.create(user_id=user_id, task_name=task_name, end_date=end_date)
#
#         data = dict(msg="Todo 생성완료", task_name=task.task_name,\
#                     start_date = task.start_date.strftime("%Y-%m-%d"),\
#                     end_date = task.end_date)
#
#
#         return Response(data = data)

# class TaskSelect(APIView):
#     def post(self, request):
#         user_id = request.data.get("user_id","")
#         tasks = Task.objects.filter(user_id=user_id)
#         task_list = []
#         for task in tasks:
#             task_list.append(dict(task_name = task.task_name, start_date = task.start_date,\
#                                   end_date = task.end_date, state = task.state))
#         return Response(dict(tasks = task_list))