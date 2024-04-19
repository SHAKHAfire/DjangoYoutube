from django import forms
from django.contrib.auth.models import User

from .models import Posts, PostComment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255, label="Post title", help_text="Title of your post"
    )
    content = forms.CharField(
        label="content",
        help_text="Post content",
        widget=forms.Textarea(attrs={"rows": 3, "cols": 50}),
    )

    class Meta:
        model = Posts
        fields = ["title", "content"]


class PostCommentForm(forms.ModelForm):
    comment_content = forms.CharField(
        label="Enter comment",
        help_text="Comment content",
        widget=forms.Textarea(attrs={"rows": 2, "cols": 50}),
    )

    class Meta:
        model = PostComment
        fields = ["comment_content"]
