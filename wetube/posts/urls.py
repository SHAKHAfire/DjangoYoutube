from django.urls import path, include

from .views import *

urlpatterns = [
    # path("", redirect_to_home),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("update_post/<int:pk>", PostUpdateView.as_view(), name="update_post"),
    # path("book_details/<int:pk>", BookDetailsView.as_view(), name="book_details"),
    # path("delete_book/<int:book_id>", delete_book, name="delete_book"),
    # path('add_to_wishlist/<int:book_id>',
    #      add_to_wishlist, name="add_to_wishlist"),
]
