from django.urls import path
from django.contrib.auth import views as auth_views
# URLs for this specific app (homework assignments)

from . import views

urlpatterns = [
    path('', views.landing),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('projects', views.projects),
    path('projects/new_project', views.new_project),
    path('projects/<str:project_name>/', views.project_view),
    path('projects/<str:project_name>/new_step', views.new_step),
    path('resources', views.resources),
    path('chat', views.chat),
    path('chat/<str:room_name>/', views.room, name='room'),
]