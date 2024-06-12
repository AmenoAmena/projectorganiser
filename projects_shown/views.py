from django.shortcuts import render
from django.http import HttpResponse
from .forms import project_form
from django.contrib.auth.decorators import login_required
from authentication.models import Project

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

def project_room(request):
    pass

def profile(request):
    pass