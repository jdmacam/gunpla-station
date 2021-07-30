from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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