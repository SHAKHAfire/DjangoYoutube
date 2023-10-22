from django.views.generic import TemplateView
from django.shortcuts import redirect, render, HttpResponse




def home_view(request):
    return render(request,template_name="home.html")
    return HttpResponse('hallo')
