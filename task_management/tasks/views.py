from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import HttpResponse


# Create your views here.

# def task_list(request):
#     tasks = Task.objects.all()
    
#     return render(
#         request,
#         'task/list.html',
#         {'tasks' : tasks}
#     )


def task_list(request):
    filter_option = request.GET.get('filter', 'all')
    if filter_option == 'completed':
        tasks = Task.objects.filter(is_completed=True)
    elif filter_option == 'not_completed':
        tasks = Task.objects.filter(is_completed=False)
    else:
        tasks = Task.objects.all() 

    return render(request, 'task/list.html', {
        'tasks': tasks,
        'filter_option': filter_option, 
    })




def task_details(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        'task': task,
    }
    
    return render(request,'task/details.html', context)

    
def home(request):
    return render(request, 'task/base.html')    


