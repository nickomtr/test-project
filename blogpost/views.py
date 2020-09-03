from django.shortcuts import render
from .models import PostText
def index(request):
    posts = PostText.objects

    return render(request, 'blogpost/index.html', {'posts':posts})
##############
##############
def post(request):
    return render(request, 'blogpost/post-opened.html')