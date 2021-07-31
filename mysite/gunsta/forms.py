from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

from . import models

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email already exists")
    return value

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProjectForm(forms.Form):
    project_title = forms.CharField(
        label="Project Title",
        required=True,
        max_length=240,
    )

    project_description = forms.CharField(
        label="Description",
        max_length=240,
    )

    def save(self, request):
        project_instance = models.ProjectModel()
        project_instance.project_title = self.cleaned_data["project_title"]
        project_instance.author = request.user
        project_instance.project_description = self.cleaned_data["project_description"]
        project_instance.save()
        return project_instance

class StepForm(forms.Form):
    step_name = forms.CharField(
        label="Step Name",
        required=True,
        max_length=240,
    )
    def save(self, request, project_title):
        project_instance = models.ProjectModel.objects.filter(author=request.user, project_title=project_title).first()
        step_instance = models.StepModel()
        step_instance.step_name = self.cleaned_data["step_name"]
        step_instance.author = request.user
        step_instance.project = project_instance
        step_instance.status = "in-progress"
        step_instance.save()
        return step_instance