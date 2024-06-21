from django.shortcuts import render
from django.http import HttpResponse
from .forms import SeeForm

# Create your views here.
def index(request):
    form = SeeForm()
    return render(request, 'show_project/index.html',{
        'form':form
    })