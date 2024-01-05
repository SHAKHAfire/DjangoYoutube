import logging
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import PostForm, PostCommentForm
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from smtplib import SMTPException
from django.core.mail import send_mail
from django.conf import settings

# from wetube.wetube.settings import


logger = logging.getLogger(__name__)

# Create your views here.
class AddPostView(CreateView):
    modal = Posts
    form_class = PostForm
    template_name = "add_post.html"

    def post(self, *args, **kwargs):
        form = self.get_form()
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            messages.success(
                self.request, f"Post {post.title} successfully created"
            )
            try:
                send_mail(
                    "Success!",
                    f"Post {post.title} successfully created",
                    settings.EMAIL_HOST_USER,
                    [post.author.email],
                    fail_silently=False,
                )
            except SMTPException as error:
                logger.critical("Error while sending email")
        return redirect(f"/posts/post-details/{post.id}")


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    modal = Posts
    form_class = PostForm
    template_name = "update_post.html"

    def get_queryset(self):
        self.success_url=f"/posts/post-details/{self.kwargs['pk']}"
        return Posts.objects.filter(id=self.kwargs["pk"])
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    modal = Posts
    form_class = PostForm
    template_name = "update_post.html"
    success_url = "/"

def redirect_to_home(request):
    return redirect("home_page")


def delete_post(request, pk: int):
    Posts.objects.get(id=pk).delete()
    messages.success(request, "Post deleted successfully!")
    return redirect("home_page")

def delete_comment(request,pk:int):
    comment=PostComment.objects.get(id=pk)
    post_id=comment.post.id
    comment.delete()    
    messages.success(request, "Comment deleted successfully!")
    return redirect(f"/posts/post-details/{post_id}")


class PostDetailsView(DetailView):
    modal = Posts
    # form_class = PostCommentForm
    template_name = "post_details.html"

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
        return redirect("/")

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs["pk"])


class CommentCreateView(CreateView):
    modal = PostComment
    form_class = PostCommentForm

    template_name = "add_post_comment.html"
    success_url = "/"

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user
            comment.content = form.cleaned_data["comment_content"]
            post_id = self.request.path.split("/")[-2]
            comment.post = Posts.objects.get(id=post_id)
            comment.save()
            messages.success(
                request=self.request,
                message=f"Commented under post {comment.post.title} successfully!")

        return redirect(
            f"/posts/post-details/{self.request.path.split('/')[-2]}")
