from django import forms
from .models import PostText
class FormPost(forms.ModelForm):
    class Meta:
        model = PostText
        fields = ('post_image' , 'post_text' , 'post_title')