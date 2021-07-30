from django.shortcuts import render, redirect
from django.contrib.auth import logout

from . import models

from . import forms
# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect('/projects')
    else:
        return redirect('/login/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    
    context = {
        "title":"Registration",
        "form":form_instance
    }
    return render(request, "registration/register.html", context=context)


def projects(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    project_objects = models.ProjectModel.objects.filter(author=request.user)
    context = {
        "title": "Gunpla Station",
        "project_objects": project_objects
    }
    return render(request, "projects.html", context=context)

def chat(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {
        "title": "Gunpla Station"
    }
    return render(request, "chat/index.html", context=context)

def resources(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {
        "title": "Gunpla Station"
    }
    return render(request, "resources.html", context=context)

def room(request, room_name):
    user = request.user.username
    return render(request, 'chat/room.html', {
        "title": "Gunpla Station",
        'room_name': room_name,
        'username': user
    })