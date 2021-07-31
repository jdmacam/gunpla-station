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
    return render(request, "projects/projects.html", context=context)

# individual project view
def project_view(request, project_name):
    if not request.user.is_authenticated:
        return redirect('/login/')

    project_object = models.ProjectModel.objects.filter(author=request.user, project_title=project_name).first()
    step_objects = models.StepModel.objects.filter(author=request.user, project=project_object)
    
    context = {
        "title": "Gunpla Station",
        "project_name": project_name,
        "project_object": project_object,
        "step_objects": step_objects
    }
    return render(request, "projects/project.html", context=context)

# new project
def new_project(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == "POST":
        form_instance = forms.ProjectForm(request.POST)
        if form_instance.is_valid():
            form_instance.save(request)
            return redirect("/projects")
    else:
        form_instance = forms.ProjectForm()
    context = {
        "form":form_instance,
    }
    return render(request, "projects/new_project.html", context=context)

# delete project
def delete_project(request, project_name):
    if not request.user.is_authenticated:
        return redirect('/login/')

    project_object = models.ProjectModel.objects.filter(author=request.user, project_title=project_name).first()
    print("*** Deleting ***" + str(project_object) + "\n\n")
    project_object.delete()

    return redirect("/projects")

# new step
def new_step(request, project_name):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == "POST":
        form_instance = forms.StepForm(request.POST)
        if form_instance.is_valid():
            form_instance.save(request, project_name)
            reurl = "/projects/" + project_name + "/"
            return redirect(reurl)
    else:
        form_instance = forms.StepForm()
    context = {
        "title": "Gunpla Station",
        "project_name": project_name,
        "form": form_instance
    }
    return render(request, "projects/new_step.html", context=context)

# update step
def update_step(request, project_name, step_name):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    project_object = models.ProjectModel.objects.filter(author=request.user, project_title=project_name).first()
    step_object = models.StepModel.objects.get(author=request.user, project=project_object, step_name=step_name)
    if step_object.status == "finished":
        step_object.status = "in-progress"
    elif step_object.status == "in-progress":
        step_object.status = "finished"
    step_object.save()
    #print("*** step_object ***" + str(step_object) + "\n\n")
    reurl = "/projects/" + project_name + "/"
    #print("*** URL REDIRECT ***" + str(reurl) + "\n\n")
    return redirect(reurl)

# delete step
def delete_step(request, project_name, step_name):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    project_object = models.ProjectModel.objects.filter(author=request.user, project_title=project_name).first()
    step_object = models.StepModel.objects.get(author=request.user, project=project_object, step_name=step_name)
    print("*** Deleting ***" + str(step_object) + "\n\n")
    step_object.delete()

    reurl = "/projects/" + project_name + "/"
    return redirect(reurl)

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
    header = ""
    print("**********" + room_name)
    if room_name == "Building":
        header = "Building Questions"
    elif room_name == "AnimeMangaTv":
        header = "Anime/Manga/TV"
    elif room_name == "Gaming":
        header = "Gaming"
    elif room_name == "AuctionHouse":
        header = "Buying/Selling"

    return render(request, 'chat/room.html', {
        "header": header,
        'room_name': room_name,
        'username': user
    })