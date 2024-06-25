from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index_show'),
    path("<str:project_token>/",views.project_room,name='show_project')
]