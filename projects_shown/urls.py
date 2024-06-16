from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("profile/", views.profile, name='profile'),
    path("project/<str:project_name>", views.project_room, name='projects'),
    path("add", views.add_project, name='add'),
    path("project/<str:project_name>/<str:feature>", views.add_feature, name="add_feature"),
    path("project/<str:project_name>/features/<int:feature_id>/done",views.done_feature, name='feature_done'),
    path("project/<str:project_name>/features/<int:feature_id>/delete",views.delete_feature, name="feature_delete"),
    path('project/<str:project_name>/', views.text_add, name='add_text'),
    path("dones",views.done_projects,name="dones"),
    path('project/<str:project_name>/finish',views.project_finish, name="finish"),
]
