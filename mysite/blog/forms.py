# coding=utf-8

from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
        widget=forms.Textarea)
    

class CommentForm(forms.ModelForm):
    name =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))
    email =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')