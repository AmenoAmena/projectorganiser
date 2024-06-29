from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SeeForm
from authentication.models import Project
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    form = SeeForm()
    if request.method == 'POST':
        form = SeeForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            try:
                project = Project.objects.get(token=token)
                return redirect('show_project:show_project', project_token=token)
            except Project.DoesNotExist:
                form.add_error('token', 'Invalid project token')
                form = SeeForm()  # Reset the form
    return render(request, 'show_project/index.html', {
        'form': form
    })

def project_room(request, project_token):
    try:
        project = Project.objects.get(token=project_token)
        features = project.features.filter(feature_done=False)
        features_done = project.features.filter(feature_done=True)
        return render(request, 'show_project/project_room.html', {
            'project': project,
            'features': features,
            'done_features': features_done,
        })
    except Project.DoesNotExist:
        return redirect('show_project:index')
