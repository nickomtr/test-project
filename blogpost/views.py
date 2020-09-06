from django.shortcuts import render, get_object_or_404
from .models import PostText

def index(request):
    posts = PostText.objects

    return render(request, 'blogpost/index.html', {'posts':posts})
##############
##############
def post(request, post_id):
    currentpost = get_object_or_404(PostText, pk = post_id)
    return render(request, 'blogpost/post-opened.html', {'posts':currentpost})