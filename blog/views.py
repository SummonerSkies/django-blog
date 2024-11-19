from django.shortcuts import render
from django.views import generic
from .models import Post

    # Create your views here.abs


    class PostList(generic.ListView):
        model = Post