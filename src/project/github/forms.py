from django import forms
from .models import Github

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Github
        fields = ['repositoryName', 'repositoryDescription']