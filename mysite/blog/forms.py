from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    # name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
        widget=forms.Textarea)