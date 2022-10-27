from socket import fromshare
from django import forms
from blog.models import Post, Restaurant

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"


        