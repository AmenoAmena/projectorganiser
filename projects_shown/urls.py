from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("profile/",views.profile,name='profile'),
    path("project/<str:project_name>",views.project_room,name='projects'),
    path("add",views.add_project,name='add'),
]