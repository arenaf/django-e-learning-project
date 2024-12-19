from django import forms
from .models import Subject, File


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "image"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject name'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'description', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'File Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'File Description'}),
            'file': forms.FileInput()
        }
