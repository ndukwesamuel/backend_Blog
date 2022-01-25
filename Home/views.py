from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


from .forms import Post_Form, Post_edit_Form

from django.urls import reverse_lazy




class HomeListView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-Date_field']


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
    template_name = "update.html"
    form_class = Post_edit_Form
    # fields = "__all__"


class Blog_DeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')



