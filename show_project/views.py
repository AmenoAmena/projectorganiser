from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import SeeForm
from authentication.models import Project

# Create your views here.
def index(request):
    form = SeeForm()
    return render(request, 'show_project/index.html',{
        'form':form
    })

def project_room(request,project_token):
    project = get_object_or_404(Project, token=project_token)
    return render(request, 'show_project/project_room.html',{
        'project':project
    })
    