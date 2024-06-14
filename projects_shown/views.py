from django.shortcuts import render
from django.http import HttpResponse
from .forms import project_form,add_project_form
from django.contrib.auth.decorators import login_required
from authentication.models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def index(request):
    user = request.user
    form = project_form()
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects_shown/index.html',{
        'form':form,
        'user':user,
        'projects':projects,
    })

def project_room(request,project_name):
    project = get_object_or_404(Project,name=project_name)
    return render(request, 'projects_shown/project.html',{
        'project':project,
    })

def profile(request):
    user = request.user
    return render(request, 'projects_shown/profile.html',{
        'user':user
    })

def add_project(request):
    form = add_project_form()
    return render(request, 'projects_shown/add.html',{
        'form':form,
    })