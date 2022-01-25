from django.urls import path

from Home.views import HomeListView, Blog_details, BlogCreateView, blog_update, Blog_DeleteView,CategoryView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),

    path('update/<int:pk>', blog_update.as_view(), name='blog_update'),
    path('delete/<int:pk>', Blog_DeleteView.as_view(), name='delete'),

    path('category/<str:cat>', CategoryView, name='category'),


    path('<int:pk>', Blog_details.as_view(), name='details'),

]
