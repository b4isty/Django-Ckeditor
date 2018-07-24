from django import forms
from django.forms import forms
from django.forms import ModelForm
from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
