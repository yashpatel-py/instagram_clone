from django import forms
from post.models import Post

from django.forms import ClearableFileInput


class NewPostForm(forms.ModelForm):
    content = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'form-control', 'placeholder': 'Please select your file'}), required=True)
    caption = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'style': 'height: 100px', 'placeholder': 'Write caption here'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter tags without "#"'}), required=True)

    class Meta:
        model = Post
        fields = ('content', 'caption', 'tags')
