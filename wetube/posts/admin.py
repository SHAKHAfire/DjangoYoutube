from django.apps import apps
from django.contrib import admin
from .models import PostComment, Post

# app = apps.get_app_config('posts')

# for model_name, model in app.models.items():
#     admin.site.register(model)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["author"]


admin.site.register(PostComment)
