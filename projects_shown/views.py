from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import project_form,add_project_form,feature_add,note_add
from django.contrib.auth.decorators import login_required
from authentication.models import Project,Feature
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
    user = request.user
    form = project_form()
    projects = Project.objects.filter(user=request.user,is_done=False)
    return render(request, 'projects_shown/index.html',{
        'form':form,
        'user':user,
        'projects':projects,
    })

@login_required
def project_room(request,project_name):
    project = get_object_or_404(Project,name=project_name)
    form =  project_form()
    features = project.features.filter(feature_done = False)
    features_done = project.features.filter(feature_done = True)
    feature_form = feature_add()
    return render(request, 'projects_shown/project.html',{
        'project':project,
        'form':form,
        'feature_form':feature_form,
        'features':features,
        'done_features':features_done,
    })

@login_required
def add_project(request):
    form = add_project_form()
    user = request.user
    if request.method == 'POST':
        form = add_project_form(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = user
            project.save()
            return redirect('projects_shown:index')
    return render(request, 'projects_shown/add.html',{
        'form':form,
    })

@login_required
def add_feature(request, project_name,feature):
    project = get_object_or_404(Project, name=project_name)
    Feature_form = feature_add()
    

    if request.method == 'POST':
        Feature_form = feature_add(request.POST)
        if Feature_form.is_valid():
            feature_name = Feature_form.cleaned_data['feature_add']
            print(feature_name)
            new_feature = Feature_form.save(commit= False)
            new_feature.feature_add = feature_name
            new_feature.save()
            project.features.add(new_feature)
            return redirect('projects_shown:projects', project_name=project_name)
    else:
        feature_form = feature_add()

    return redirect('projects_shown:projects', project_name=project_name)

@login_required
def done_feature(request,project_name,feature_id):
    project = get_object_or_404(Project, name=project_name)
    feature = get_object_or_404(Feature, pk=feature_id)
    
    if request.method == 'POST':    
        feature.feature_done = True
        feature.save()

    return redirect('projects_shown:projects', project_name=project_name)

@login_required
def delete_feature(request, project_name,feature_id):
    project = get_object_or_404(Project, name = project_name)
    feature = get_object_or_404(Feature, pk = feature_id)

    if request.method == 'POST':
        feature.delete()    

    return redirect('projects_shown:projects', project_name=project_name)

@login_required
def text_add(request, project_name):
    project = get_object_or_404(Project, name=project_name)

    if request.method == 'POST':
        new_notes = request.POST.get('text-area', '') 
        project.notes = new_notes  
        project.save()  

        return redirect('projects_shown:projects', project_name=project_name)

    return redirect('projects_shown:projects', project_name=project_name)

@login_required
def done_projects(request):
    projects = Project.objects.filter(is_done = True)
    return render(request,"projects_shown/done.html",{
        'projects':projects
        })

@login_required
def sure(request,project_name):
    project = get_object_or_404(Project,name = project_name)
    return render(request,"projects_shown/sure.html",{
        'project':project
    })

@login_required
def finish(request,project_name):
    project = get_object_or_404(Project,name = project_name)
    project.is_done = True
    project.save()
    return redirect("projects_shown:index")

@login_required
def done_show(request,project_name):
    project = get_object_or_404(Project,name = project_name)
    features_done = project.features.filter(feature_done = True)
    return render(request,"projects_shown/done_project.html",{
        'project':project,
        'features':features_done,
    })

def feature_page(request,project_name,feature_id):
    feature = get_object_or_404(Feature,id=feature_id)
    project = get_object_or_404(Project,name=project_name)
    return render(request,"projects_shown/feature_page.html",{
        'feature':feature,
        'project':project,
    })