from django import forms

from stories.models import Story

from django.forms import ClearableFileInput


class NewStoryForm(forms.ModelForm):
    content = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'form-control', 'placeholder': 'Please select your file'}), required=True)
    caption = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Story
        fields = ('content', 'caption')
