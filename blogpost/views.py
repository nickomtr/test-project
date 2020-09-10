from django.shortcuts import render, get_object_or_404, redirect
from .models import PostText
from .forms import FormPost
from django.utils import timezone
def index(request):
    posts = PostText.objects

    return render(request, 'blogpost/index.html', {'posts':posts})
##############
##############
def post(request, post_id):
    currentpost = get_object_or_404(PostText, pk = post_id)
    return render(request, 'blogpost/post-opened.html', {'posts':currentpost})
def new_post(request):
    if request.method == 'POST':
        form = FormPost(request.POST)
        if form.is_valid():
            print('1111111111111111111111111111111111')
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('')
    else:
        print('22222222222222222222222222222222222222')
        form = FormPost()


    return render(request, 'blogpost/newpost.html', {'form':form})