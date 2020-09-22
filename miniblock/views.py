from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    if request.user.is_authenticated:
        print('1')
    else:
        print('2')
    return render(request, 'auth.html')


