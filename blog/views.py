from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
) 
from . models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,
                                        UserPassesTestMixin
                                        )
from django.contrib.messages.views import SuccessMessageMixin
'''
def home(request):
    posts = Post.objects.all()  # This is a list of posts

    context={
        'posts': posts,
        'title': 'List of Posts',
    }

    return render(request, 'blog/home.html', context)
'''
class PostListView(ListView):  # <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    login_url = '/login/'
    paginate_by = 3

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post    
    login_url = '/login/'
def about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'blog/about.html', context)

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    login_url = '/login/'
    success_message = "Post created successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    login_url = '/login/'
    success_message = "Post updated successfully!"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    login_url = '/login/'
    success_message = "Post deleted successfully!"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author