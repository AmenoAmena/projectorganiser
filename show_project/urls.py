from django.urls import path
from . import views

app_name = 'show_project'

urlpatterns = [
    path("",views.index,name='index_show'),
    path("<str:project_token>/",views.project_room,name='show_project')
]