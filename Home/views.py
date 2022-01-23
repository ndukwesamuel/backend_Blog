from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post





class HomeListView(ListView):
    model = Post
    template_name = "index.html"


class Blog_details(DetailView):
    model = Post
    template_name = "details.html"


