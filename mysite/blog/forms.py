# coding=utf-8

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
        widget=forms.Textarea)
    

    # def send_mail(self):
        # cd = self.cleaned_data
        # post_url = request.build_absolute_uri(post.get_absolute_url())
        # subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
        # message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
        # send_mail(subject, message, 'admin@myblog.com',[cd['to']])