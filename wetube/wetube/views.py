from django.views.generic import TemplateView
from django.shortcuts import redirect, render, HttpResponse
from posts.models import Posts


def home_view(request):
    context = {"posts": Posts.objects.all()[::-1]}
    for i in Posts.objects.filter(author=None):
        i.delete()

    return render(request, template_name="home.html", context=context)


def titles_view(request):
    return render(request, "titles.html")
