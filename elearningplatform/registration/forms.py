from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Email required.")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repeat Password'})
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email already exists.")
        return email


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Profile.objects.filter(is_teacher=False)

    class Meta:
        model = Profile
        fields = ["avatar", "subjects", "students"]
        widgets = {
            'subjects': forms.SelectMultiple(attrs={'class': 'form-control mb-3'}),
            'students': forms.SelectMultiple(choices=Profile.objects.all(), attrs={'class': 'form-control mb-3'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "subjects"]
        widgets = {
            'subjects': forms.SelectMultiple(attrs={'class': 'form-control mb-3'})
        }
