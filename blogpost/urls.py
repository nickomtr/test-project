
from django.urls import path
from .models import PostText
from . import views
urlpatterns = [

    path('', views.index),
    path('<int:post_id>/', views.post, name='post_opened'),
    path('newpost/', views.new_post, name='new_post')
]
