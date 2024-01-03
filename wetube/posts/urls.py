from django.urls import path, include

from .views import *


urlpatterns = [
    # path("", redirect_to_home),
    path("/add_post/", AddPostView.as_view(), name="add_post"),
    path(
        "/update_post/<int:pk>", PostUpdateView.as_view(), name="update_post"
    ),
    path("/delete_post/<int:post_id>", delete_post, name="delete_post"),
    path(
        "/post-details/<int:pk>",
        PostDetailsView.as_view(),
        name="post_details",
    ),
    path(
        "/post-details/<int:pk>/add-comment",
        CommentCreateView.as_view(),
        name="add-comment",
    ),
]
