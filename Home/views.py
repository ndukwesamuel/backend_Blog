from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post


from .forms import Post_Form





class HomeListView(ListView):
    model = Post
    template_name = "index.html"


class Blog_details(DetailView):
    model = Post
    template_name = "details.html"




class BlogCreateView(CreateView):
    model = Post
    form_class = Post_Form
    template_name = "create.html"
    # fields = "__all__"



class blog_update(UpdateView):
    model = Post
    template_name = "create.html"
    form_class = Post_edit_Form
    # fields = "__all__"




