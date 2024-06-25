from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import SeeForm
from authentication.models import Project

# Create your views here.
def index(request):
    form = SeeForm()
    if request.method == 'POST':
        form = SeeForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            return redirect('show_project', project_token=token) 
    return render(request, 'show_project/index.html',{
        'form':form
    })

def project_room(request,project_token):
    project = get_object_or_404(Project,token=project_token)
    features = project.features.filter(feature_done = False)
    features_done = project.features.filter(feature_done = True)
    return render(request, 'show_project/project_room.html',{
        'project':project,
        'features':features,
        'done_features':features_done,
    })
