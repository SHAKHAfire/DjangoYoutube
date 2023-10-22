from django.views.generic import TemplateView
from django.shortcuts import redirect, render




def home_view(request):
    return render(request, "home.html")
