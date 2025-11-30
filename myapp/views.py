from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request, id):
    projects = list(Project.objects.values())
    return JsonResponse(projects.index(id), safe=False)

def hello(request, id):
    print(type(id))
    result = (id + 200) * 3
    return HttpResponse("<h1>Hello %s</h1>" % result)

def about(request):
    return HttpResponse("About")

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('Task: %s'  % task.title)

def index2(request):
    return HttpResponse("<H1>hOLA</h1>")