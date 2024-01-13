from django.urls import path, include

from .views import *


urlpatterns = [
    # path("", redirect_to_home),
    path("add-post/", AddPostView.as_view(), name="add_post"),
    path(
        "update-post/<int:pk>", PostUpdateView.as_view(), name="update_post"
    ),
    path(
        "update-comment/<int:pk>", CommentUpdateView.as_view(), name="update_comment"
    ),
    path("delete-post/<int:pk>", delete_post, name="delete_post"),

    path("delete-comment/<int:pk>", delete_comment, name="delete_comment"),
    
    path(
        "post-details/<int:pk>",
        PostDetailsView.as_view(),
        name="post_details",
    ),
]
