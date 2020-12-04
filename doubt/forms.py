from django import forms

class PostQuery(forms.Form):
    title = forms.CharField()
    detail = forms.TextField(widget=forms.Textarea)