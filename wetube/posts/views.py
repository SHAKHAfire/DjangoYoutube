
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import PostForm
from .models import Posts
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# from wetube.wetube.settings import

# Create your views here.
class AddPostView(CreateView):
    modal = Posts
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = 'home_page'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
        return redirect('home_page')
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    modal = Posts
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs['pk'])

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def redirect_to_home(request):
    return redirect('home_page')

def delete_post(request, post_id: int):
    post = Posts.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('http://127.0.0.1:8000/')

class PostDetailsView(DetailView):
    modal = Posts
    template_name = 'post_details.html'

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs['pk'])
